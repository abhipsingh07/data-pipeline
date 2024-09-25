import pandas as pd
import json
import sqlite3

def load_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data

def load_json_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    table = pd.DataFrame(data)
    return table


def load_sql_data(database_path, query):
    connection = sqlite3.connect(database_path)
    data = pd.read_sql_query(query, connection)
    connection.close()
    return data

def combine_data_sources(data_sources):
    combined_data = pd.DataFrame()  # Create an empty DataFrame
    for source in data_sources:
        if source['type'] == 'csv':
            data = load_csv_file(source['path'])  # Load CSV data
        elif source['type'] == 'json':
            data = load_json_file(source['path'])  # Load JSON data
        elif source['type'] == 'sql':
            data = load_sql_data(source['path'], source['query'])  # Load SQL data
        combined_data = pd.concat([combined_data, data], ignore_index=True)
    return combined_data

if __name__ == "__main__":
    data_sources = [
        {'type': 'csv', 'path': 'data/export_of_join_employee_and_department_tables.csv'},
        {'type': 'json', 'path': 'data/employee_department_data.json'},
        {'type': 'sql', 'path': 'data/sqlite.db', 'query': 'SELECT * FROM employee'}
    ]

    # Combine the data from all sources
    final_table = combine_data_sources(data_sources)

    # Write the final combined data to a CSV file
    final_table.to_csv('combined_output.csv', index=False)

    print("Data has been successfully written to 'combined_output.csv'")
