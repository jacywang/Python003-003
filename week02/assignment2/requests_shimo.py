from fake_useragent import UserAgent
from time import sleep
import requests

user_agent = UserAgent(verify_ssl=False)
headers = {
  'User-Agent': user_agent.random,
  'Referer': 'https://shimo.im/login?from=home'
}

# Persist cookie
s = requests.Session()

# Get cookie
pre_login_url = "https://shimo.im/welcome"
s.get(pre_login_url, headers=headers)

sleep(1)

login_url = 'https://shimo.im/lizard-api/auth/password/login'
form_data = {
  'email': 'email@example.com',
  'password': 'password',
  'mobile': '+86undefined'
}

response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)

sleep(1)

profile_url = 'https://shimo.im/profile'
response2 = s.get(profile_url, headers=headers, cookies=s.cookies)
print(response2.status_code)