import os

from django.shortcuts import resolve_url
from django.db.models import Q

from .models import Project, Cost


# SEARCH
###############################################################################

class SearchServicesPage():
    """ Class for searching in html files """

    def __init__(self, filepath, title, url_name):
        self.filepath = filepath
        self.title = title
        self.url_name = url_name

    def get_url(self):
        return resolve_url(self.url_name)

    def get_file(self):
        with open(self.filepath, 'rb') as file:
            lines = file.readlines()
        return lines

    def search_word(self, word):
        file = self.get_file()
        for line in file:
            if word in line.decode('utf-8').lower():
                return True
        return False


# services_urls is a list of html files to search
# ('main', 'templates', 'main') doesn't work on servers
templates_path = (os.path.dirname(__file__), 'templates', 'main')
services_urls = [
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'services', 'bp.html'),
        # filepath='main/templates/main/services/bp.html',
        title=str('Разработка бизнес-плана и финансовой модели инвестиционного'
                  ' проекта'),
        url_name='service_bp_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'services', 'cmr.html'),
        title='Классические маркетинговые исследования',
        url_name='service_cmr_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'services', 'mmr.html'),
        title='Современные маркетинговые исследования',
        url_name='service_mmr_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'services', 'mo.html'),
        title='Аутсорсинг маркетинга',
        url_name='service_mo_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'services', 'msc.html'),
        title='Управленческий и стратегический консалтинг',
        url_name='service_msc_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'services', 'woem.html'),
        title='Оптимизация сайтов и email-рассылка',
        url_name='service_woem_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'about_us.html'),
        title='О нас',
        url_name='about_us_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'dictionary.html'),
        title='Словарь',
        url_name='dictionary_url'
    ),
    SearchServicesPage(
        filepath=os.path.join(*templates_path, 'index.html'),
        title='Домашняя страница',
        url_name='homepage_url'
    )
]


def search(word, files=services_urls):
    """ Keyword search in selected content """

    word = word.lower()
    out = []
    for search_class in files:
        if search_class.search_word(word):
            out.append({
                'title': search_class.title,
                'url': search_class.get_url()
            })

    # search in the Project model
    projects = Project.objects.filter(
        Q(title__icontains=word) | Q(title__icontains=word.capitalize()) |
        Q(title__icontains=word.upper()) |
        Q(content__icontains=word) | Q(content__icontains=word.capitalize()) |
        Q(content__icontains=word.upper())
    ).distinct()
    if projects:
        for project in projects:
            out.append({
                'title': project.title,
                'url': project.get_absolute_url()
            })

    # search in the Cost model
    costs = Cost.objects.filter(
        Q(title__icontains=word) |
        Q(title__icontains=word.capitalize()) |
        Q(title__icontains=word.upper())
    ).distinct()
    if costs:
        for cost in costs:
            out.append({
                'title': 'Цены',
                'url': resolve_url('prices_url')
            })
            break

    return out
