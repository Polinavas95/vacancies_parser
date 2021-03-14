import requests
from bs4 import BeautifulSoup

ITEMS = 100
URL = f'https://hh.ru/search/vacancy?st=searchVacancy&text=Python+junior+developer&items_on_page={ITEMS}'

# headers для обхода защиты
headers = {
  'Host': 'hh.ru',
  'User-Agent': 'Safari',
  'Accept': '*/*',
  'Accept-Endcoding': 'gzip, defalate, br',
  'Connection': 'keep-alive'
}


def get_all_pages_hh():
    # get-запрос информации со страницы
    hh_request = requests.get(
      f'{URL}',
      headers=headers
    )

    pages = []

    # получение информации в виде текста с html-страницы
    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

    # поиск и сбор информации по тегу span с определенным классом
    paginator = hh_soup.find_all('span', {'class': 'pager-item-not-in-short-range'})

    for page in paginator:
        pages.append(int(page.find('a').text))

    # получение последней страницы со всех вакансий
    return pages[-1]


def extract_job(html):
    title = html.find('a').text
    link = html.find('a')['href']
    company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).text.strip()
    location = html.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text
    return {'Должность': title, 'Компания': company, 'Место': location, 'Ссылка': link}


# сбор вакансий с каждой страницы
def get_elements_from_hh(last_page):
    jobs = []
    for page in range(last_page):
        print(f'HeadHunter: Парсинг страницы {page}')
        result = requests.get(f'{URL}&page={page}', headers=headers)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'vacancy-serp-item'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
