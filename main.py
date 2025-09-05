from fastapi import FastAPI
from data import Data
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": ""}


@app.get("/api/generate-data-and-save")
async def generate_data():
    # Simulate data generation
    data = Data()
    data.load_unpaid()
    data_folder = os.getenv("DATA_FOLDER", "./data")
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    # filename shouldbe of form "yyyymmdd.xlsx"
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"unpaid_data_{date_str}.xlsx"

    # calculate full path to save file
    full_path = data_folder + '/' + filename
    data.save_unpaid_as_excel(full_path)

    # calculate csv filename
    csv_filename = f"unpaid_data_{date_str}.csv"
    csv_full_path = data_folder + '/' + csv_filename
    data.save_unpaid_as_csv(csv_full_path)
    # clear data from memory
    data = None
    return {"message": f"Data saved to {csv_full_path}"}
