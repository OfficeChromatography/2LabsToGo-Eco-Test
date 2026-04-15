#sql for python
#This file must be in the folder 2LabsToGo-Eco-Software/app

#import os
import os
# import the sqlite3 module
import sqlite3

# Create a connection object
connection = sqlite3.connect("db.sqlite3")

# Get a cursor
cursor = connection.cursor()

# Add columns
addColumn1 = "ALTER TABLE sampleapp_pressuresettings_db ADD COLUMN rinsingFactor"
addColumn2 = "ALTER TABLE sampleapp_bandscomponents_db ADD COLUMN sampleFactor"

#cursor.execute(addColumn1)
#cursor.execute(addColumn2)

# close the database connection
connection.close()

#delete 0001_initial.py in migrations of sampleapp, finecontrol, development, detection
if os.path.exists("./sampleapp/migrations/0001_initial.py"):
  os.remove("./sampleapp/migrations/0001_initial.py")
else:
  print("The file does not exist")
  
if os.path.exists("./finecontrol/migrations/0001_initial.py"):
  os.remove("./finecontrol/migrations/0001_initial.py")
else:
  print("The file does not exist")

if os.path.exists("./development/migrations/0001_initial.py"):
  os.remove("./development/migrations/0001_initial.py")
else:
  print("The file does not exist")
  
if os.path.exists("./detection/migrations/0001_initial.py"):
  os.remove("./detection/migrations/0001_initial.py")
else:
  print("The file does not exist")

