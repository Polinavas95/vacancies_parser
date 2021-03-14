import csv


def save_to_csv(jobs):
    file = open('test.csv', mode='w')
    # Записи данных в CSV по указанным столбцам
    writer = csv.writer(file)
    writer.writerow(['Должность', 'Компания', 'Место', 'Ссылка'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return 'Успешное завершение записи'