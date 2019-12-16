import pyperclip

from mechanize import Browser
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
    url = input('Enter the link: ')

    try:
        title = get_title(url)
    except Exception:
        title = '"blocked by capcha"'

    result = TEMPLATE.format(
        title=title, url=url, date=datetime.now().strftime('%d.%m.%Y')
    )
    pyperclip.copy(result)

    print(f'"{result}" already on the clipboard!')
