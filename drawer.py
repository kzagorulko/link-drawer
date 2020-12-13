import pyperclip

from mechanize import Browser, BrowserStateError
from datetime import datetime

# Правительство Российской Федерации: официальный сайт. – Москва. – URL: http://government.ru (дата обращения: 19.02.2020). – Текст: электронный.
# История России, всемирная история: сайт. – URL: http://www.istorya.ru (дата обращения: 15.10.2019). – Текст: электронный.

TEMPLATE = (
    '{title}. – URL: {url} (дата обращения: {date}). – Текст: электронный.'
)


def get_title(url):
    br = Browser()
    br.open(url)
    return br.title()


if __name__ == '__main__':
    url = input('Enter the link: ')

    try:
        title = get_title(url)
    except BrowserStateError:
        print("can't fetch relative reference: not viewing any document")
        title = '"enter your title"'
    except Exception as e:
        if '403' in str(e):
            print("HTTP Error 403")
        title = '"enter your title"'

    result = TEMPLATE.format(
        title=title, url=url, date=datetime.now().strftime('%d.%m.%Y')
    )
    pyperclip.copy(result)

    print(f'"{result}" already on the clipboard!')
