import requests

def upload_video_to_facebook(page_id, access_token, video_path, description):
    url = f"https://graph-video.facebook.com/v12.0/{page_id}/videos"
    params = {
        'access_token': access_token,
        'description': description,
    }
    files = {
        'source': open(video_path, 'rb')
    }
    response = requests.post(url, params=params, files=files)
    return response.json()

page_id = '115619794921708'
access_token = 'EAAOV6w29jiYBO9q8taG5AQIcgZCGZBpfspwcyumdZBn7rVW6c7JHC2hzBHZBdVnjzfvIzmYTTVZBXiMLgER6ZCGU6uOvU2ZCZAfWQwOigDps2TYZBwShNw6DviBWkbR4ZBubK152wwxfZCm3tNmKa9Yc0mt5eOA8L6b5e1juA5ZCriAXp0qEwjueJrSdpa5kMdgbwniVZBwmcSvi7cdJLYfZBw4ndAZAJjSgyZAZBszqCNarqe2oZD'
video_path = r'C:\Users\pheas\Desktop\the-tools-modules\postReel\for-testing\video 0.mp4'
description = 'Your video description #hashtag1 #hashtag2'

result = upload_video_to_facebook(page_id, access_token, video_path, description)
print(result)
