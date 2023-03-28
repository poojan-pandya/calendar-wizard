# calendar-wizard
Python script which generates .ics calendar events from a shorthand text input format resembling a to-do list, making it easier to schedule events and tasks for the upcoming day.
## How to use
1. Install packages
```console
pip install ics arrow
```

2. Run the script
```console
python3 main.py [-f filename]
```

3. Enter events in the following format:
```
[start time (e.g. 3:00pm)] [end time] [event name]
```
Input can be supplied line-by-line via the command line or through a text file with the -f flag. (See `sampleinput.txt`)

The default date for each event is today's date and the default time zone is US/Eastern. If you'd like to change the timezone, please change the TIMEZONE constant in `main.py`. Supported values are listed [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

4. Import the generated .ics file in any supported calendar client (e.g. iCal, Outlook, Google Calendar)

## Future Work
* Allow the user to specify the timezone
* Add functionality for all day events
* Add functionality for alarms
* Add "native" time zone support instead of GMT offset
* Support more forms of date input
* Add support for events which span multiple days
* Host the tool on the web
