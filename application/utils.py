def upload_file_s3(s3_client, file, bucket):
    response = s3_client.upload_file(file, bucket, file)
    return response


def list_files(s3_client, bucket, location):
    files = list()
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            files.append(f"{location}{item['Key']}")
    except Exception as e:
        pass
    return files
