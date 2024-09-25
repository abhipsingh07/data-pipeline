Data Combiner Tool
What does this tool do?
This tool helps us put data from different places together:

A CSV file 
A JSON file 
An SQL database 

How do we use this tool?
Step 1: Get our files ready
We need three types of files:

A CSV file (like export_of_join_employee_and_department_tables.csv)
A JSON file (like employee_department_data.json)
An SQL file (like sqlite.db)
We put all these files inside a folder called data.


Step 2: Check the paths in the code
Open the tool’s code file called injestion_tool.py in PyCharm.

In the code, there is a part that looks like this:

data_sources = [
    {'type': 'csv', 'path': 'data/export_of_join_employee_and_department_tables.csv'},
    {'type': 'json', 'path': 'data/employee_department_data.json'},
    {'type': 'sql', 'path': 'data/sqlite.db', 'query': 'SELECT * FROM employee'}
]


If our file names are different, we can change them here to match the files we have.


Step 3: Run the tool in PyCharm
In PyCharm, we can run the code by doing the following:
Right-click on the ingestion_tool.py file inside PyCharm.
click on Run 'ingestion_tool'.
PyCharm will run the code, and we will see the output at the bottom.


Step 4: Check the output
After running the tool, it will make a new CSV file called combined_output.csv.

Message like:
Data has been successfully written to 'combined_output.csv'

We can now open this file and see all the data combined into one table