from SampleDict import employee_data
import csv
import boto3
import json

access_key = 'AKIA4SMENIVZLJIH7SOZ'
secret_key = '8AAgIA0V9uRMdzH5MH9fmzDMCNQ3z2e9jLm84FgK'
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)



#COVERT TO CSV
field_names = ['Name'] + list(employee_data[next(iter(employee_data))].keys())
with open('employee_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(field_names)
    for name, data in employee_data.items():
        row = [name] + [data[field] for field in field_names[1:]]
        writer.writerow(row)
print("Converted To CSV")
with open('employee_data.csv', 'r') as csvfile:
    contents = csvfile.read()
    print(contents) 



#UPLOAD TO S3
bucket_name = 'lambda-test-buc'
s3.upload_file('employee_data.csv', bucket_name, 'employee_data.csv')
print("CSV file uploaded successfully.\n") 



#DOWNLOAD FROM S3
bucket_name = 'lambda-test-buc'
file_key = 'employee_data.csv'
download_path = 'downloaded_employee_data.csv'
s3.download_file(bucket_name, file_key, download_path)
print("File downloaded successfully.")

with open('downloaded_employee_data.csv', 'r') as csvfile:
    contents = csvfile.read()
    print(contents)



#BACK TO DICTIONARY
download_path = 'downloaded_employee_data.csv'
employee_data = {}
with open(download_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name']
        data = {field: row[field] for field in row if field != 'Name'}
        employee_data[name] = data
print("Converted back to Dictionary")
print(employee_data)



#DICT TO JSON DUMP
output_file = 'employee_data.json'
with open(output_file, 'w') as json_file:
    json.dump(employee_data, json_file)
print("JSON file created successfully.")