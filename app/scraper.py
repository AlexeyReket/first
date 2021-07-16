import requests
from bs4 import BeautifulSoup

url = 'https://idp.grsu.by/simplesaml/module.php/core/loginuserpass.php?AuthState=_0b15103dd86ab2582b3b42e58df7db991b2af328ed%3Ahttps%3A%2F%2Fidp.grsu.by%2Fsimplesaml%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fedu.grsu.by%252Fauth%252Fsaml2%252Fsp%252Fmetadata.php%26RelayState%3Dhttps%253A%252F%252Fedu.grsu.by%252Fauth%252Fsaml2%252Flogin.php%253Fwants%253Dhttps%25253A%25252F%25252Fedu.grsu.by%25252Fmy%25252F%26cookieTime%3D1626433625'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div')


print(quotes)
