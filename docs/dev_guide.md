## Installation

First, download the required packages using:

`pip3 install -r requirements.txt`

## Setting up

To run the program, you need to create the database:

`$ sqlite3 quiz.db < quiz.sql`

Then, you need to create a CSV file named "users.csv" with the users that will be added to the database. Then run:

`python3 adduser.py`

Finally, to run the application:

`sudo python3 softdes.py`

## Code structure

The main code is located in "softes.py". You can find the available routes with flask annotation and suport functions to handle specific runtime requirements.

The student code will be run on the "lambda_handler" function.

The file "adduser.py" inserts in the database the users on the CSV file.