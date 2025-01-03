# Work-Schedule-Creator
This takes in a CSV file of employee availability and returns a CSV of a possible schedule. It will warn about gaps in availability for certain shifts. 

The columns in the input CSV file are name, week, availability (for all shifts), and number of shifts wanted. 

User inputs chosen week and CSV file. Then, a downable photo is displayed.

Example Google Form that would create a useable CSV file: [https://forms.gle/iKpVQvPCc6yi3jMS9](url)

Likely future features:
- handle availability at two locations (no overlapping shifts)
- user can set up: input their own column names

Possible future features:
- displays several schedule options
- allows for changes (like swaps of shifts, or clicking to open possible replacements)
- return the most optimation schedule
- allows for the option to favor pairs between coworkers or ensure two people never work together (will need to handle if there are not possible schedules, and warning and alert for needed person)
