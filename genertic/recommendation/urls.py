from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^ql/$', views.q_learning, name='q_learning'),
    url(r'^click/(?P<name>.*)/(?P<rule>.*)$', views.click, name='click'),
    # url(r'^inf$', views.fill_in, name='inf'),
    # url(r'^search/$',views.search, name="search"),
    # url(r'^employer-search/$',views.employer_search, name="employer_search"),
    # url(r'^job-create/$',views.create_job, name="create_job"),
    # url(r'^job/(?P<job_name>.*)/(?P<job_id>\d+)$',views.job_detail, name="job_detail"),
    # url(r'^detail/(?P<job_name>.*)/(?P<job_id>\d+)/(?P<noti_id>\d+)$',views.click_noti, name="click_noti"),
    # url(r'^profile/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.disable_detail, name="dis_detail"),
    # url(r'^request-job/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.invite_job_to_disability, name="request_job"),
    # url(r'^contactus/$',views.contact, name="contactus"),
    # url(r'^search-job/$', views.disable_search_job, name='disable_search_job'),
    # url(r'^search-disability-person/$', views.employer_search_disability, name='employer_search_disability'),
    # url(r'^notifications/$',views.notification_mobile, name="noti"),
    # url(r'^confirm/(?P<job_name>.*)/(?P<job_id>\d+)$',views.confirm_job, name="confirm_job"),
    # url(r'^confirm_job/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.confirm_job, name="confirm_job"),
    # url(r'^apply_job/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.apply_job, name="apply_job"),
    # url(r'^notificationsall/$',views.show_notifications, name="show_notifications"),
    # url(r'^refuse_job/(?P<dis_id>\d+)/(?P<job_id>\d+)$',views.refuse_job, name="refuse_job"),
    # url(r'^isSave/$', views.company_save_disable, name='company_save_disable'),
    # url(r'^disIsSave/$', views.disable_save_job, name='disable_save_job'),
    # url(r'^question/$', views.question, name='question'),

]
