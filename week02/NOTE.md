学习笔记

## Pretty errors

[Documentation](https://pypi.org/project/pretty-errors/)

## How to handle exceptions

`try` [documentation](https://docs.python.org/3.7/reference/compound_stmts.html#the-try-statement)

`with` [documentation](https://docs.python.org/3.7/reference/compound_stmts.html#the-with-statement)

## Save data into MySQL

[PyMySQL](https://pypi.org/project/PyMySQL/) is recommended.

## Fake User Agent

```
from fake_useragent import UserAgent
from time import sleep
import requests

user_agent = UserAgent(verify_ssl=False)
headers = {
  'User-Agent': user_agent.random,
  'Referer': 'https://shimo.im/login?from=home'
}
```

## Selenium and webdriver
[Documentation](https://www.selenium.dev/selenium/docs/api/py/)

## HTTP Proxy
See [assignment1](https://github.com/jacywang/Python003-003/tree/master/week02/assignment1).

## Distributed crawling
[scrapy-redius](https://github.com/rmax/scrapy-redis)