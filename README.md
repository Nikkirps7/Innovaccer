# InnovaccerAnalytics
Name: Matcha Nikhil
B.Tech 3rd year(Mathematics and Computing)
IIT Guwahati

First run the code.py and keep track of the location of the file new_names1.csv and then run the file1.py(the location of the file new_names1.csv is used here)


Summary of the approach:
Duplicate entry differ from original entry only in first name and last name, where as date of birth and gender remain same.
So it is sufficient to make changes only in first names and last names.
The name of the duplicate entry will vary from the original entry once a space occurs.
i.e before the occurrence of space, both duplicate entry and original entry are same.
Therefore we will convert all the duplicate entries to corresponding original ones(i.e without having space) so that we can delete them easily.
We will store them in a different file from where we will delete all the identical ones.
