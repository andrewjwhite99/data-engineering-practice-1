import os
import requests
import zipfile
import io

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
] 

def unzip_to_folder(list_of_uris, target_directory):
    for uri in list_of_uris:
        req = requests.get(uri)
        if req.ok:
            zip = zipfile.ZipFile(io.BytesIO(req.content))
            zip.extractall(target_directory)
        else:
            print("The file you are trying to access does not exist")




def main():
    # Create downloads directory
    current_directory = os.getcwd()
    directory_name = "downloads"
    target_directory = os.path.join(current_directory, directory_name)

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    unzip_to_folder(download_uris, target_directory)

    


if __name__ == '__main__':
    main()
