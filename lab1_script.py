import requests

# Print requests library version
print('requests library version is', requests.__version__)
print()

# Send GET request to Google homepage, print response text
res = requests.get("http://www.google.com")
print("response text for GET request to Google homepage:", end="\n\n")
print(res.text, end="\n\n")

# Download itself from Github and print its own source code
res = requests.get("https://raw.githubusercontent.com/olivier-vadiaval/CMPUT404Fall2021-Lab1/main/lab1_script.py")
print("Python script source code from Github:", end="\n\n")
print(res.text)
