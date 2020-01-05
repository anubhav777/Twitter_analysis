from django.urls import path,include
from rest_framework import routers
from .views import Displaypages,modified_get,ad_data,insert_pages,graph,date_end,get_allads,try_function,ads_page_display,country_list,ads_analysis,social_tracker,monthly_average,blob
from apscheduler.schedulers.background import BackgroundScheduler
from .files import timeout
scheduler=BackgroundScheduler()
job=None
router=routers.DefaultRouter()
router.register('pages',Displaypages)


urlpatterns = [
   path('',include(router.urls)),


  
]

# def start_job():
#     global job
#     job=scheduler.add_job(timeout,'interval',minutes=30)
#     try:
#         scheduler.start()
#     except :
#         pass
# start_job()