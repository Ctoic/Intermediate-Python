import requests
from datetime import datetime

# Replace YOUR_USERNAME and YOUR_PAT with your actual Github username and personal access token
username = 'ctoic'
pat = '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'

# Make a GET request to the Github API to get information about your account
response = requests.get(f'https://api.github.com/users/{ctoic}', auth=(ctoic, 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))
data = response.json()

# Get the date and time when you joined Github
created_at = datetime.fromisoformat(data['created_at'].replace('Z', '+00:00'))

# Get the current date and time
now = datetime.now()

# Calculate the time difference between the current date and time and the date and time when you joined Github
time_on_github = now - created_at

# Display the time you spent on Github in days, hours, and minutes
print(f'Time on Github: {time_on_github.days} days, {time_on_github.seconds // 3600} hours, {time_on_github.seconds % 3600 // 60} minutes')







