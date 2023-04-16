# User modules

- When your programs get larger or you work in a team, You will want to structure your code by splitting it into separate source files.
- There are two reasons why this split becomes necessary.
  - large programs can consist of hundreds of functions that become difficult to manage and debug if they are all in one source file.
  - It would be very difficult for multiple programmers to edit a single source file simultaneously in a team.
- Large Python programs typically consist of a driver module and one or more supplemental modules.
  - The driver module contains the main function or the first executable statement if no main function is used.
  - The supplemental modules contain supporting functions and constant variables.
- To see modules in action, refer to special_topic in chapter 8 of the source code.
  - To run the program execute the driver module using the command: `python salesreport.py`.
  