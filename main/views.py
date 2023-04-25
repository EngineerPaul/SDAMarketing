import os
from datetime import date
import random

from django.views.generic import (
    TemplateView, ListView, DetailView
)
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from .models import (
    Cost, CostGroup, Project, Direction, Industry,
    Vacancy, Slider, SiteContent
)
from .serializers import ProjectListSerializer, FeedbackFormSerializer
from .services import search, convert_query_to_dict, common_site_content


class Homepage(TemplateView):
    template_name = os.path.join('main', 'index.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel_path'] = os.path.join('main', 'inc', '_carousel.html')
        context['slider'] = list(Slider.objects.all())
        random.shuffle(context['slider'])
        page_content = [
            'homepage_content', 'homepage_left_text', 'homepage_btn_text',
            'homepage_col1_title', 'homepage_col1_content',
            'homepage_col2_title', 'homepage_col2_content',
            'homepage_col3_title', 'homepage_col3_content',
            'homepage_col4_title', 'homepage_col4_content'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class About_us_page(TemplateView):
    template_name = os.path.join('main', 'about_us.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'about_us_title', 'about_us_content'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Services_page(TemplateView):
    template_name = os.path.join('main', 'services.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'services_title', 'services_content', 'services_link1',
            'services_link2', 'services_link3', 'services_link4',
            'services_link5', 'services_link6'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


# 6 next classes like Service_page_... are 6 services page

class Service_page_MSC(TemplateView):
    """ Service page of Management and strategic consulting """
    template_name = os.path.join('main', 'services', 'msc.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'services_link1', 'services_1'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Service_page_CMR(TemplateView):
    """ Service page of Classic Marketing Research """
    template_name = os.path.join('main', 'services', 'cmr.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'services_link2', 'services_2'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Service_page_MMR(TemplateView):
    """ Service page of Modern marketing research """
    template_name = os.path.join('main', 'services', 'mmr.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'services_link3', 'services_3'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Service_page_MO(TemplateView):
    """ Service page of Marketing outsourcing """
    template_name = os.path.join('main', 'services', 'mo.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'services_link4', 'services_4'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Service_page_WOEM(TemplateView):
    """ Service page of Website optimization and email marketing """
    template_name = os.path.join('main', 'services', 'woem.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'services_link5', 'services_5'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Service_page_BP(TemplateView):
    """ Service page of Business plans """
    template_name = os.path.join('main', 'services', 'bp.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'services_link6', 'services_6'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Prices_page(ListView):
    """ Page of prices. Uses 2 models: Cost and CostGroup """

    model = CostGroup
    context_object_name = 'costgroups'
    template_name = os.path.join('main', 'prices.html')

    def get_queryset(self):
        """ Function return two dicts of cost groups (CostGroup model)
        and costs (Cost model):
        - dict of all services without 'another services'
        - dict of 'another services' """
        initial_queryset = self.model.objects.all().prefetch_related('cost')

        services, another_services = dict(), dict()
        for group in initial_queryset:
            if str(group) != "<p>Другие услуги</p>":
                services[group] = group.cost.all()
            else:
                another_services['title'] = group
                another_services['costs'] = group.cost.all()

        return {'services': services, 'another_services': another_services}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'Prices_title', 'Prices_content', 'Prices_footer'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class ProjectsPageView(TemplateView):
    """ Page of all projects. Content is loaded by asynchronous JS requests.
    Context directions and industies are filters of queryset. Handles the
    request class ProjectListAPI. """

    template_name = os.path.join('main', 'projects.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directions'] = Direction.objects.all()
        context['industries'] = Industry.objects.all()

        page_content = [
            'projects_title', 'projects_left_content', 'projects_btn_text',
            'projects_kind_filter', 'projects_industry_filter'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class ProjectDetail(DetailView):
    """ Page of specific project description """

    model = Project
    template_name = os.path.join('main', 'projectdetail.html')
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'projects_title', 'projectdetail_title', 'projectdetail_diretion',
            'projectdetail_industry'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class SearchView(TemplateView):
    """ Search page in website content """

    template_name = os.path.join('main', 'search.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        keyword = self.request.GET.get('search')
        context['search_list'] = search(keyword)

        page_content = [
            'search_title', 'search_by_word', 'search_nothing'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        context['content']['search_by_word'].value = context[
            'content']['search_by_word'].value % context['search']
        context['content']['search_nothing'].value = context[
            'content']['search_nothing'].value % context['search']
        return context


# class Vacancies_page(ListView):
class Vacancies_page(TemplateView):
    """ Page of vacancies """

    # model = Vacancy
    context_object_name = 'vacancies'
    template_name = os.path.join('main', 'vacancies.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'vacancies_title', 'vacancies_content'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Contacts_page(TemplateView):
    """ Page of contacts """
    template_name = os.path.join('main', 'contacts.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'contacts_title', 'contacts_content'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


class Dictionary_page(TemplateView):
    """ Page of terms definitions """
    template_name = os.path.join('main', 'dictionary.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_content = [
            'dictionary_title', 'dictionary_content'
        ]
        site_content = common_site_content + page_content
        site_content = SiteContent.objects.filter(name__in=site_content)
        site_content = convert_query_to_dict(site_content)
        context['content'] = site_content
        context['content']['footer'].value = context[
            'content']['footer'].value % date.today().year
        return context


# API
###############################################################################

class ProjectPaginationAPI(PageNumberPagination):
    """ Pagination of projects by request pages """

    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 30


class ProjectListAPI(ListAPIView):
    """ API class for fetch requests project page. Query params direction and
    industry are filters for queryset. """

    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectListSerializer
    permission_classes = [AllowAny]
    pagination_class = ProjectPaginationAPI

    def get_queryset(self):
        queryset = self.queryset
        directions = self.request.GET.getlist('direction')
        industries = self.request.GET.getlist('industry')
        if directions:
            queryset = queryset.filter(
                direction__pk__in=directions
            )
        if industries:
            queryset = queryset.filter(
                Q(industry__pk__in=industries) | Q(industry__title="Все отрасли")
            )
        return queryset.select_related('direction')


class SendFeedBackAPI(APIView):
    """ View get feedback with js (feedback.js) and send message to email """

    serializer_class = FeedbackFormSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.send(
            name=serializer.data['name'],
            contact=serializer.data['contact'],
            text=serializer.data['text'],
            link=serializer.data['link'],
        )
        return Response(
            status=status.HTTP_200_OK
        )

    def send(self, name, contact, text, link):
        message = str(
            f'Имя пользователя: {name}\n'
            f'Контакт: {contact}\n'
            f'Ссылка: {self.request.get_host()}{link}\n'
            f'Сообщение: {text}\n'
        )
        send_mail(
            subject='Запрос с сайта',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_RECEIVER_USER],
            fail_silently=False
        )
