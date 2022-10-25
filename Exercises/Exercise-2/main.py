import requests
import pandas as pd
import re
import os


def lines_that_contain(target_string: str, string_to_search: str) -> list:
    matching_strings = []
    for line in string_to_search.split("\n"):
        if target_string in line:
            matching_strings.append(line)
    return matching_strings


def create_download_folder():
    current_directory = os.getcwd()
    directory_name = "downloads"
    target_directory = os.path.join(current_directory, directory_name)

    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    return target_directory


def download_file_to_specified_directory(url, file_name, target_directory):
    """Downloads file from the url and save it as filename"""
    file_path = os.path.join(target_directory, file_name)
    # Check if file already exists
    if not os.path.isfile(file_path):
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(f"{file_path}", "wb") as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)


def main():
    # your code here
    target_directory = create_download_folder()

    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    target_last_modified = "2022-02-07 14:03"

    response = requests.get(url)
    text = response.text

    line_list = lines_that_contain(target_last_modified, text)

    file_list = []

    for line in line_list:
        file = re.search('href="(.*?)">', line).group(1)
        file_list.append(file)

    for file in file_list:
        file_url = url + file
        download_file_to_specified_directory(file_url, file, target_directory)

    # Now only doing one of these files
    df = pd.read_csv(target_directory + "/" + file_list[0])

    max_hourly_dry_bulb_temperature_index = df["HourlyDryBulbTemperature"].idxmax()

    print(df.loc[[max_hourly_dry_bulb_temperature_index]])


if __name__ == "__main__":
    main()
