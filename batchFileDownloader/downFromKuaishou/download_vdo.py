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

if __name__ == "__main__":
    # Example usage
    url = 'https://v2.kwaicdn.com/ksc2/brTdxIV1D1ZabSMHabSt_t5wjokb8G33g6BpNhstjJSc0lvhYqIlBzCzE-RQfITGn5wH2ry08vHFRq9BsQVE0Y7FtzULtl44GOERfPKFdqcs7ebaw9xiSkdPYkNC9AjSJhPxhTir_qtCXvBp7mdVs78Af9v3OvznEJ2IRzORVhp4Hx_4Q2KXUkVUUaLz0AGH.mp4?pkey=AAXM6OvPc8E738VmfomIXHF38lJx9SZ32oXc_EsxEfQvmDkIIb4Kw2o8buaB8_9FBDAn0pE5LYebCx6vdCEqYJ9pImVreP10RIL79Qf77PR1qxKkjjS6nynJckYQBJCXDRc&tag=1-1725648474-unknown-0-uzdljrybim-74b347dc8577f2a3&clientCacheKey=3xjqn6quvd7vc5a_b.mp4&di=af64643c&bp=14734&tt=b&ss=vp.mp4'  # Replace with your video URL
    folder_path = './videos'  # The folder where you want to save the video
    file_name = 'my_video.mp4'  # The name you want to save the file as

    # Call the function
    download_video(url, folder_path, file_name)
