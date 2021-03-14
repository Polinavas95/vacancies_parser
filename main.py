from head_hunter import get_all_pages_hh, get_elements_from_hh
from so import get_all_pages_so, get_elements_from_so
from save import save_to_csv

# Методы получения всех вакансий с каждой страницы
hh_jobs = get_elements_from_hh(get_all_pages_hh())
so_jobs = get_elements_from_so(get_all_pages_so())

all_jobs = hh_jobs + so_jobs

save_to_csv(all_jobs)