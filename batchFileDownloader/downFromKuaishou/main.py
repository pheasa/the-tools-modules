import json
import os
import glob
import inquirer
import enlighten

import requests

def download_video(url, file_name, folder_path='./videos'):
    # Send a request to the video URL
    response = requests.get(url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Combine folder path and file name to get the full file path
        file_path = f"{folder_path}/{file_name}"
        
        # Open a file for writing binary content
        with open(file_path, 'wb') as video_file:
            # Write content chunk by chunk to avoid memory overload for large files
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    video_file.write(chunk)
        print(f"Video downloaded successfully: {file_path}")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")

json_files = glob.glob('*.json')
json_files.append('Exit')

# Create a list of choices for the user
list_file_json = [
    inquirer.List('file',
                  message="Select a JSON file",
                  choices=json_files,
                 ),
]
# Prompt the user to select a file
selected_file = inquirer.prompt(list_file_json)

if selected_file and selected_file['file'] != 'Exit':
    only_name = os.path.splitext(selected_file['file'])[0]
    # Open and read the JSON file
    with open(selected_file['file'], 'r') as file:
        if not os.path.isdir(only_name):
            os.mkdir(only_name)
            video_links = json.load(file)  # Load the file content as a Python dictionary or list
            manager = enlighten.Manager()
            pbar = manager.counter(total=10)
            for index in pbar(range(len(video_links))):
                folder_path = f'./{only_name}'  # The folder where you want to save the video
                # Call the function
                download_video(video_links[index], f'video {index}.mp4', folder_path)
        else:
            print(f'Folder name {only_name} is file already exists!')
