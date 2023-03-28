"""
File: calendar.py
Author: Poojan Pandya

This script creates a .ics file from text input in a
short-hand format, enabling quick creation of calendar
events.

Format: [start time (e.g. 3:00pm)] [end time] [event name]

Command Line Args:
[None] - The script collects input line-by-line from the
command line

-f [filename] - The script reads input from the specified
file path

TODO List:
    - Allow user to enter date instead of automatically using
      today's date
    - Add functionality for all day events
    - Add functionality for alarms
    - Add "native" time zone support instead of GMT offset
"""

import sys
import arrow
from ics import Calendar, Event


SENTINEL = ''
INTERNAL_TIME_FORMAT = 'M-D-YYYY h:mmA'
TIMEZONE = 'US/Eastern'


def add_event(input, cal):
    """
    Add a single event to the calendar. Checks for invalid input.
    
    @param input (str): formatted string
    @param cal (Calendar): Calendar object to be modified
    """
    # get the current month, day, year to use in all events
    now = arrow.utcnow().to(TIMEZONE)
    month, day, year = now.month, now.day, now.year
    splits = input.split()
    if len(splits) < 3:
        print(f'Invalid input {input}. Event not added.')
        return
    e = Event()
    e.name = ' '.join(splits[2:])
    begin_datetime = f'{month}-{day}-{year} {splits[0]}'
    end_datetime = f'{month}-{day}-{year} {splits[1]}'
    try:
        e.begin = arrow.get(begin_datetime, INTERNAL_TIME_FORMAT, tzinfo=TIMEZONE)
        e.end = arrow.get(end_datetime, INTERNAL_TIME_FORMAT, tzinfo=TIMEZONE)
    except arrow.parser.ParserMatchError:
        print(f'Invalid input {input}. Event not added.')
        return
    cal.events.add(e)
    print(f'Added event: {input}')


def fill_calendar_file(filename, cal):
    """
    Process input from a text file and add events to the Calendar
    
    @param filename (str): File containing formatted input
    @param cal (Calendar): Calendar object to be modified
    """
    with open(filename) as file:
        for line in file:
            line = line.strip()
            add_event(line, cal)
            

def fill_calendar_user(cal):
    """
    Add events to Calendar from user input, entered one line at a time

    @param cal (Calendar): Calendar object to be modified
    """
    print('Enter your events one line at a time in the following format:')
    print('[start time (e.g. 3:00pm)] [end time] [name]\n\n')
    while True:
        inp = input('Enter your event (blank line to stop): ')
        if inp == SENTINEL: break
        add_event(inp, cal)
        

def main():
    cal = Calendar()
    args = sys.argv[1:]
    if args:
        if args[0] == '-f':
            if len(args) >= 2:
                filename = args[1]
                fill_calendar_file(filename, cal)
            else:
                raise Exception('Must provide file name')
        else:
            raise Exception('Invalid flag')
    else:
        fill_calendar_user(cal)
    with open('my.ics', 'w') as file:
        file.writelines(cal.serialize_iter())


if __name__ == '__main__':
    main()