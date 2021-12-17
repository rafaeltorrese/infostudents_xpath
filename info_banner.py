import requests
import lxml.html as html

URL_HOME = ''
XPATH_NAMES = '//table[3]/tbody/tr/td[2]/span/text()'
XPATH_ID = '//table[3]/tbody/tr/td[3]/span/text()'
XPATH_EMAIL = '//table[3]/tbody/tr/td[8]/span/a/@href'


if __name__ == '__main__':
    pass