import pyarrow.parquet as pq
import pandas as pd

"""
path = input("Enter the json file path: ")
data = pq.read_table(path)

df = data.to_pandas()

csv_save_path = input("Enter the path where you want to save the converted csv file along with the file name: ")
df.to_csv(csv_save_path)

"""
df = pd.read_csv("data/python_code_instructions.csv")

jsonl_save_path = "data/python_code_instructions.jsonl"

df.to_json(jsonl_save_path, orient='records', lines=True)