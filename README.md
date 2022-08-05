# Timetable-Generator
This python based web application generates the time-table for multiple courses using a  single input.

Input:- Excel file containing details of Course code, Subject name, Teachers Name, Class/Week.

Output:- Single excel file containing multiple sheets. Each sheets contains timetable for a
         different course. Time table is in 5*4 grid (5 days and 4 class slots).

Problem it solves
- It makes the process of scheduling hassle free.
- Avoids human error such as scheduling same professor in two different classes on same time.
- Arranges the subjects in a way that everyday is interesting.

Instructions for operation

- Open the app directory and run cmd for that directory
- Type "python app.py" and hit enter (don't use "")
- Address to the local host would flash on screen, copy and paste on web browser 
- Open the website. 
- Download the pre-prepared format of excel file from the given link and fill in the columns with
  appropriate details.

- Upload the prepared input excel (xls) file.
      ** MAKE SURE THE FILE YOU ARE UPLOADING MUST BE IN THE SAME DIRECTORY AS THE MAIN PROGRAM**

- The output excel file containing timetables for different courses will be automatically
  downloaded.

Constraints:
- The input excel file has a fixed layout, and is of type xls.
- The name of teacher, if repeated in multiple courses; should be same at all places. 
- Spelling and abbreveations must be consistent through out.
- The excel file you need to upload must be in same directory of the main.py function.

Possible errors:
- File format
- File directory 
- Summation (Class/Week) >20
- Unique subject and teacher names (SoCT, SOCT,soct and all other combinations will be considered as soct)
