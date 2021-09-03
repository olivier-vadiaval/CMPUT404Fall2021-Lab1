import requests

# Print requests library version
print('requests library version is', requests.__version__)
print()

# Send GET request to Google homepage, print response text
res = requests.get("http://www.google.com")
print("response text for GET request to Google homepage:", end="\n\n")
print(res.text)
