import pyperclip

from mechanize import Browser, BrowserStateError, _response
from datetime import datetime

TEMPLATE = (
    '{title} [Электронный ресурс] – Заглавие с экрана. – Режим доступа: {url}.'
    ' (Дата обращения: {date}).'
)


def get_title(url):
    br = Browser()
    br.open(url)
    return br.title()


if __name__ == '__main__':
    # url = input('Enter the link: ')
    url = ''

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
