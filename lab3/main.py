from pathlib import Path
from datetime import datetime
import numpy as np
import pandas as pnd
import csv
import random as rand
import matplotlib.pyplot as plt
from credentials import *


def create_data(path: Path) -> None:
    rows_amount: int = rand.randint(1000, 2000)
    with open(path, 'w', encoding='utf-16', newline='') as file:
        titles = [
            'Табельный номер',
            'Фамилия И.О.',
            'Пол',
            'Год рождения',
            'Год начала работы в компании',
            'Подразделение',
            'Должность',
            'Оклад',
            'Количество выполненных проектов'
        ]
        file_writer = csv.DictWriter(file, fieldnames=titles)
        file_writer.writeheader()
        for i in range(1, rows_amount + 1):
            gen: str = rand.choice(gender)
            if gen == 'Мужской':
                full_name = rand.choice(male_last_name) + ' ' + rand.choice(male_first_name) + ' ' + rand.choice(
                    male_middle_name)
            else:
                full_name = rand.choice(female_last_name) + ' ' + rand.choice(female_first_name) + ' ' + rand.choice(
                    female_middle_name)
            year_of_birth: int = rand.randint(1970, 2002)
            year_of_start_working: int = year_of_birth + rand.randint(18, 20)
            subdivision: str = rand.choice(subdivisions)
            job_title: str = rand.choice(job_titles)
            salary: int = rand.randrange(15000, 50000, 1000)
            project_amounts: int = rand.randint(1, 20)
            file_writer.writerow({
                'Табельный номер': i,
                'Фамилия И.О.': full_name,
                'Пол': gen,
                'Год рождения': year_of_birth,
                'Год начала работы в компании': year_of_start_working,
                'Подразделение': subdivision,
                'Должность': job_title,
                'Оклад': salary,
                'Количество выполненных проектов': project_amounts
            })


def create_statistics_lists(path: Path) -> None:
    with open(path, 'r', encoding='utf-16') as file:
        project_amounts: list[int] = []
        salaries: list[int] = []
        years_of_birth: list[int] = []
        years_of_start_working: list[int] = []
        subdivisions: list[str] = []

        file_reader = csv.DictReader(file)
        for line in file_reader:
            project_amounts.append(int(line['Количество выполненных проектов']))
            salaries.append(int(line['Оклад']))
            years_of_birth.append(int(line['Год рождения']))
            years_of_start_working.append(int(line['Год начала работы в компании']))
            subdivisions.append(line['Подразделение'])

        work_experiencies: list[int] = [datetime.now().year - years_of_start_working[i]
                                        for i in range(len(years_of_birth))]

        print('')
        print('***СТАТИСТИКА NUMPY***')
        print('')
        print(f'Количество сотрудников (чел.): {np.count_nonzero(work_experiencies)}')
        print('')
        print('СТАТИСТИКА ПО ОПЫТУ РАБОТЫ')
        print('')
        print(f'Максимальный стаж (лет): {np.max(work_experiencies)}')
        print(f'Минимальный стаж (лет): {np.min(work_experiencies)}')
        print(f'Средний стаж (лет): {round(np.average(work_experiencies), 2)}')
        print('')
        print('СТАТИСТИКА ПО КОЛИЧЕСТВУ ПРОЕКТОВ')
        print('')
        print(f'Максимальное количество проектов на сотрудника (шт.): {np.max(project_amounts)}')
        print(f'Минимальное количество проектов на сотрудника (шт.): {np.min(project_amounts)}')
        print(f'Среднее количество проектов на сотрудника (шт.): {round(np.average(project_amounts), 2)}')
        print(f'Суммарное количество проектов (шт.): {np.sum(project_amounts)}')
        print('')
        print('СТАТИСТИКА ПО ЗАРПЛАТЕ')
        print('')
        print(f'Максимальная зарплата (руб.): {np.max(salaries)}')
        print(f'Минимальная зарплата (руб.): {np.min(salaries)}')
        print(f'Средняя зарплата (руб.): {round(np.average(salaries), 2)}')
        print(f'Сумма зарплат (руб.): {np.sum(salaries)}')
        print(f'Среднее арифметическое значение зарплаты (руб.): {round(np.mean(salaries), 2)}')
        print(f'Медианное значение зарплаты (руб.): {np.median(salaries)}')
        print(f'Дисперсия зарплаты (руб.): {round(np.var(salaries), 2)}')
        print(f'Стандартное отклонение зарплаты (руб.): {round(np.std(salaries), 2)}')
        print('')
        print('СТАТИСТИКА ПО ОТДЕЛАМ')
        print('')
        print(f'Количество отделов: {len(np.unique(subdivisions))}')
        print(f'Количество сотрудников в отделе Java разработки: {np.count_nonzero(np.array(subdivisions) == "Отдел Java разработки")}')
        print(f'Количество сотрудников в отделе Python разработки: {np.count_nonzero(np.array(subdivisions) == "Отдел Python разработки")}')
        print(f'Количество сотрудников в отделе .NET разработки: {np.count_nonzero(np.array(subdivisions) == "Отдел .NET разработки")}')
        print(f'Количество сотрудников в отделе frontend разработки: {np.count_nonzero(np.array(subdivisions) == "Отдел frontend разработки")}')
        print(f'Количество сотрудников в отделе PHP разработки: {np.count_nonzero(np.array(subdivisions) == "Отдел PHP разработки")}')
        print(f'Количество сотрудников в отделе Android разработки: {np.count_nonzero(np.array(subdivisions) == "Отдел Android разработки")}')
        print(f'Количество сотрудников в отделе IOS разработки: {np.count_nonzero(np.array(subdivisions) == "Отдел IOS разработки")}')
        print('')


def create_statistics_pnd(path: Path) -> None:
    company = pnd.read_csv(path, encoding='utf-16')
    print('***СТАТИСТИКА PANDAS***')
    print('')
    print(f'Количество сотрудников (чел.): {company["Табельный номер"].count()}')
    print('')
    print('СТАТИСТИКА ПО КОЛИЧЕСТВУ ПРОЕКТОВ')
    print('')
    print(f'Максимальное количество проектов на сотрудника (шт.): {company["Количество выполненных проектов"].max()}')
    print(f'Минимальное количество проектов на сотрудника (шт.): {company["Количество выполненных проектов"].min()}')
    print(f'Среднее количество проектов на сотрудника (шт.): {round(company["Количество выполненных проектов"].sum() / company["Табельный номер"].count(), 2)}')
    print(f'Суммарное количество проектов (шт.): {company["Количество выполненных проектов"].sum()}')
    print('')
    print('СТАТИСТИКА ПО ЗАРПЛАТЕ')
    print('')
    print(f'Максимальная зарплата (руб.): {company["Оклад"].max()}')
    print(f'Минимальная зарплата (руб.): {company["Оклад"].min()}')
    print(f'Средняя зарплата (руб.): {round(company["Оклад"].sum() / company["Оклад"].count(), 2)}')
    print(f'Сумма зарплат (руб.): {company["Оклад"].sum()}')
    print(f'Среднее арифметическое значение зарплаты (руб.): {round(company["Оклад"].mean(), 2)}')
    print(f'Медианное значение зарплаты (руб.): {company["Оклад"].median()}')
    print(f'Дисперсия зарплаты (руб.): {round(company["Оклад"].var(), 2)}')
    print(f'Стандартное отклонение зарплаты (руб.): {round(company["Оклад"].std(), 2)}')
    print('')
    print('СТАТИСТИКА ПО ОТДЕЛАМ')
    print('')
    print(f'Количество отделов: {len(np.unique(subdivisions))}')
    print(f'Количество сотрудников в отделе Java разработки: {len(company[company["Подразделение"] == "Отдел Java разработки"])}')
    print(f'Количество сотрудников в отделе Python разработки: {len(company[company["Подразделение"] == "Отдел Python разработки"])}')
    print(f'Количество сотрудников в отделе .NET разработки: {len(company[company["Подразделение"] == "Отдел .NET разработки"])}')
    print(f'Количество сотрудников в отделе frontend разработки: {len(company[company["Подразделение"] == "Отдел frontend разработки"])}')
    print(f'Количество сотрудников в отделе PHP разработки: {len(company[company["Подразделение"] == "Отдел PHP разработки"])}')
    print(f'Количество сотрудников в отделе Android разработки: {len(company[company["Подразделение"] == "Отдел Android разработки"])}')
    print(f'Количество сотрудников в отделе IOS разработки: {len(company[company["Подразделение"] == "Отдел IOS разработки"])}')
    print('')


def graphic_statistics(path: Path) -> None:
    company = pnd.read_csv(path, encoding='utf-16')
    projects_statistics = {}
    jobs = company['Должность'].unique()

    for item in jobs:
        subdiv_employees = company[company['Должность'] == item]
        projects_statistics[item] = round(subdiv_employees['Количество выполненных проектов'].sum() / subdiv_employees['Количество выполненных проектов'].count(), 2)

    plt.plot(company["Оклад"], label='Оклад')
    plt.axhline(y=np.nanmean(company['Оклад'].mean()), color='red', linestyle='--', linewidth=2, label='Mean')
    plt.title('Динамика зарплаты и среднее значение зарплаты', loc='center')
    plt.show()

    plt.bar(projects_statistics.keys(), projects_statistics.values())
    plt.title('Количество выполненных проектов по должностям', loc='center')
    plt.show()

    plt.hist(company['Подразделение'], bins=15)
    plt.title('Количесство сотрудников по отделам', loc='center')
    plt.show()


file_path = Path(Path.cwd(), 'company.csv')
create_data(file_path)
create_statistics_lists(file_path)
create_statistics_pnd(file_path)
graphic_statistics(file_path)
