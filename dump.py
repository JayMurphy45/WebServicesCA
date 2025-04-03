
import os
import json
from datetime import datetime
from pymongo import MongoClient
from zipfile import ZipFile

def create_database_dump():
    # Connect to MongoDB
    client = MongoClient("mongodb://root:example@localhost:27017/")
    db = client["CA"]  
    collection = db["products"] 

    # Fetch all records from the collection
    records = list(collection.find({}))

    # Save the records to a JSON file
    dump_file = "database_dump.json"
    with open(dump_file, "w") as f:
        json.dump(records, f, default=str, indent=4)  

    # Create a zip file with the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"database-{timestamp}.zip"
    with ZipFile(zip_filename, "w") as zipf:
        zipf.write(dump_file)

    # Clean up the JSON dump file
    os.remove(dump_file)

    print(f"Database dump created and zipped as: {zip_filename}")

if __name__ == "__main__":
    create_database_dump()