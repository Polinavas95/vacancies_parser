import requests
from bs4 import BeautifulSoup

URL = 'https://stackoverflow.com/jobs?q=junior+python+developer'


def get_all_pages_so():
    request = requests.get(URL)
    # Получение html-страницы в виде текста
    soup = BeautifulSoup(request.text, 'html.parser')
    # определение последней страницы
    last_page = int(soup.find('div', {'class', 's-pagination'}).find_all('a')[-2].get_text(strip=True))
    return last_page


def extract_job(html):
    title = html.find('h2').find('a').text
    company, location = html.find('h3').find_all('span', recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html['data-jobid']
    # Получение ссылки
    link = f'https://stackoverflow.com/jobs/{job_id}'
    return {'Должность': title, 'Компания': company, 'Место': location, 'Ссылка': link}


# Получение определенный элементов с каждой из страниц
def get_elements_from_so(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Stackoverflow: Парсинг страницы {page}')
        result = requests.get(f'{URL}&pg={page + 1}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': '-job'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
