from django.urls import path

from .views import (
    # Templates
    Homepage, About_us_page, Services_page, Prices_page, ProjectsPageView,
    ProjectDetail, SearchView, Vacancies_page, Contacts_page, Dictionary_page,
    Service_page_MSC, Service_page_CMR, Service_page_MMR,
    Service_page_MO, Service_page_WOEM, Service_page_BP,

    # Forms
    FeedBackFormView,

    # DRF
    ProjectListAPI,
)

urlpatterns = [
    path("", Homepage.as_view(), name='homepage_url'),

    # menu
    path("about-us", About_us_page.as_view(), name='about_us_url'),
    path("services", Services_page.as_view(), name='services_url'),
    path("prices", Prices_page.as_view(), name='prices_url'),
    path('projects', ProjectsPageView.as_view(),
         name='projects_url'),
    path('projects/search', SearchView.as_view(),
         name='project_search_url'),
    path('projects/<str:slug>', ProjectDetail.as_view(),
         name='project_detail_url'),
    path("vacancies", Vacancies_page.as_view(), name='vacancies_url'),
    path("contacts", Contacts_page.as_view(), name='contacts_url'),
    path("dictionary", Dictionary_page.as_view(), name='dictionary_url'),

    # services
    path("services/strategicheskij-konsalting",
         Service_page_MSC.as_view(), name='service_msc_url'),
    path("services/marketingovye-issledovania",
         Service_page_CMR.as_view(), name='service_cmr_url'),
    path("services/sovremennyie-marketingovyie-issledovaniya",
         Service_page_MMR.as_view(), name='service_mmr_url'),
    path("services/autsorsing-marketinga",
         Service_page_MO.as_view(), name='service_mo_url'),
    path("services/optimizatsia-saitov-spb",
         Service_page_WOEM.as_view(), name='service_woem_url'),
    path("services/biznes-plan-investicionnogo-proekta",
         Service_page_BP.as_view(), name='service_bp_url'),

    # forms
    path("feedback/redirect", FeedBackFormView.as_view(),
         name='feedback_redirect_url'),

    # API
    path("api/project-list", ProjectListAPI.as_view(),
         name='project_list_api_url'),
]
