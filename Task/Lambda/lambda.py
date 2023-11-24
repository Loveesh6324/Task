import csv
import boto3
import json 
import tempfile

access_key = 'AKIA4SMENIVZLJIH7SOZ'
secret_key = '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'
bucket_name = 'lambda-test-buc'
file_key = 'employee_data.csv'
output_file_key = 'employee_data.json'

s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

def lambda_handler(event, context):
    from SampleDict import employee_data

    # Convert to CSV
    field_names = ['Name'] + list(employee_data[next(iter(employee_data))].keys())

    # Create a temporary file to store the CSV
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(field_names)
        for name, data in employee_data.items():
            row = [name] + [data[field] for field in field_names[1:]]
            writer.writerow(row)
    
        # Upload CSV to S3
        csvfile.flush()
        s3.upload_file(csvfile.name, bucket_name, file_key)
        
    with open(csvfile.name, 'r') as csv_file:
        csv_contents = csv_file.read()
        print("Dict Converted to CSV")
        print(csv_contents)    

    # Download CSV from S3
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        s3.download_file(bucket_name, file_key, temp_file.name)
        print("CSV Uploaded to S3")

        # Convert CSV back to dictionary
        employee_data = {}
        with open(temp_file.name, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['Name']
                data = {field: row[field] for field in row if field != 'Name'}
                employee_data[name] = data

        # Convert dict to JSON
        json_data = json.dumps(employee_data)
        print("CSV Converted to Dict")
        print(json_data)
        
        # Upload JSON to S3
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as output_file:
            output_file.write(json_data)
            output_file.flush()
            s3.upload_file(output_file.name, bucket_name, output_file_key)

    return {
        'statusCode': 200,
        'body': 'Data processed successfully and uploaded to S3.'
    }
