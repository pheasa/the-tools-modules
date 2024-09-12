app_id = 'your_app_id'
redirect_uri = 'your_redirect_uri'
permissions = 'public_profile,email'

login_url = f'https://www.facebook.com/v17.0/dialog/oauth?client_id={app_id}&redirect_uri={redirect_uri}&scope={permissions}'
print('Login URL:', login_url)
