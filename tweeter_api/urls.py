from django.urls import path,include
from .views import insert_user,insert_timeline
urlpatterns={
    path('twitteruser/',insert_user),
    path('twittertimeline/',insert_timeline)
}
