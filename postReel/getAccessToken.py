import requests

user_access_token = 'EAAOV6w29jiYBO8VZBQFX5bZBI9e1SpLw8mY2M6gE7GGohZCCjs5kptZBCFjzhsNOFoZAMGQdCNRMwYOmfYVqvDox77O0RQOOTEnoE6zqNXa3lNWltifGQlYnNHjsvhjDZBGp9Sk7iPzzKCNduLDhU04eiZCmgp26rBHjGN7ENTZCZBT2GcTNbZB9552XFJeJoEfdnuSxZAZAozeHP9lCBxPt4iBLne2Ji0kUVcJIkNHZAww3vbeUZD'
url = f'https://graph.facebook.com/v17.0/me/accounts?access_token={user_access_token}'

response = requests.get(url)
data = response.json()
print(data)

# Extract the page access token for your page
page_access_token = None
for page in data['data']:
    print('Page Information-----------------------')
    print(f'Page Name: {page["name"]}')
    print(f'Page ID: {page["id"]}')
    print(f'Page Token: {page["access_token"]}')
