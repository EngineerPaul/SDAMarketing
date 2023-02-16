import os
from typing import List

from django.views.generic import (
    TemplateView, ListView, RedirectView, DetailView
)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormMixin

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from .models import (
    Cost, CostGroup, Article, Direction, Industry,
    Vacancy, FeedBack,
)
from .forms import FeedBackForm
from .serializers import ArticleListSerializer


class Homepage(TemplateView):
    template_name = os.path.join('main', 'index.html')


class About_us_page(TemplateView):
    template_name = os.path.join('main', 'about_us.html')


class Services_page(TemplateView):
    template_name = os.path.join('main', 'services.html')


# 6 next classes like Service_page_... are 6 services page

class Service_page_MSC(TemplateView):
    """ Service page of Management and strategic consulting """
    template_name = os.path.join('main', 'services', 'msc.html')


class Service_page_CMR(TemplateView):
    """ Service page of Classic Marketing Research """
    template_name = os.path.join('main', 'services', 'cmr.html')


class Service_page_MMR(TemplateView):
    """ Service page of Modern marketing research """
    template_name = os.path.join('main', 'services', 'mmr.html')


class Service_page_MO(TemplateView):
    """ Service page of Marketing outsourcing """
    template_name = os.path.join('main', 'services', 'mo.html')


class Service_page_WOEM(TemplateView):
    """ Service page of Website optimization and email marketing """
    template_name = os.path.join('main', 'services', 'woem.html')


class Service_page_BP(TemplateView):
    """ Service page of Business plans """
    template_name = os.path.join('main', 'services', 'bp.html')


class Prices_page(ListView):
    """ Page of prices. Uses 2 models: Cost and CostGroup """

    model = CostGroup
    context_object_name = 'costgroups'
    template_name = os.path.join('main', 'prices.html')

    def get_queryset(self):
        """ Function return dict of cost groups (CostGroup model) and costs
        (Cost model) """
        queryset = self.model.objects.all().prefetch_related('cost')
        queryset = {group: group.cost.all() for group in queryset}
        return queryset


class ArticlesPageView(TemplateView):
    """ Page of all articles. Content is loaded by asynchronous JS requests.
    Context directions and industies are filters of queryset. Handles the
    request class ArticleListAPI. """

    template_name = os.path.join('main', 'articles.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directions'] = Direction.objects.all()
        context['industries'] = Industry.objects.all()
        return context


class ArticleDetail(DetailView):
    """ Page of specific article description """

    model = Article
    template_name = os.path.join('main', 'articledetail.html')
    context_object_name = 'article'


class SearchView(ListView):
    model = Article
    context_object_name = 'search_list'
    template_name = os.path.join('main', 'search.html')

    def get_queryset(self):
        return self.model.objects.filter(
            title__icontains=self.request.GET.get('search').upper()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context


class Vacancies_page(ListView):
    """ Page of vacancies """

    model = Vacancy
    context_object_name = 'vacancies'
    template_name = os.path.join('main', 'vacancies.html')


class Contacts_page(TemplateView):
    """ Page of contacts """
    template_name = os.path.join('main', 'contacts.html')


class Dictionary_page(TemplateView):
    """ Page of terms definitions """
    template_name = os.path.join('main', 'dictionary.html')


class FeedBackFormView(RedirectView):
    """ Form for feedback that opens using message icon """

    model = FeedBack
    form = FeedBackForm

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            return self.form_valid(request, form)
        else:
            return self.get(request, *args, **kwargs)

    def form_valid(self, request, form, *args, **kwargs):
        obj = self.model()
        obj.name = form.cleaned_data['name']
        obj.contact = form.cleaned_data['contact']
        obj.text = form.cleaned_data['text']
        obj.link = form.cleaned_data['link']
        obj.save()
        return self.get(request)


# ADMIN ONLY

class AdminAccessMixin:
    """ Admin access only. Other users go to the homepage """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('homepage_url')
        return super().dispatch(request, *args, **kwargs)


class FeedBackAdminView(AdminAccessMixin, ListView):
    """ Page for viewing user messages by admin. To go, you must also click on
    the message icon. Display only not answered message """

    model = FeedBack
    context_object_name = 'feedbacks'
    template_name = os.path.join('main', 'admin', 'feedback.html')

    def get_queryset(self):
        queryset = super().get_queryset().filter(answered=False)
        return queryset


class FeedBackAnsweredFormView(RedirectView):
    """ This view make the feedback answered and remove it from feedback page.
    The class is called when admin clicks on the cross on the right side of
    the feedback table. Messages are not removed from the db """

    pattern_name = 'feedback_url'
    model = FeedBack

    def post(self, request, pk, *args, **kwargs):
        self.answered(pk)
        return self.get(request, *args, **kwargs)

    def answered(self, pk):
        obj = self.model.objects.get(pk=pk)
        obj.answered = True
        obj.save()


# API

class ArticlePaginationAPI(PageNumberPagination):
    """ Pagination of articles by request pages """

    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 10


class ArticleListAPI(ListAPIView):
    """ API class for fetch requests article page. Query params direction and
    industry are filters for queryset. """

    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleListSerializer
    permission_classes = [AllowAny]
    pagination_class = ArticlePaginationAPI

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
                industry__pk__in=industries
            )
        return queryset
