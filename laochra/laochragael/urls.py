from django.urls import path 

from . import views


urlpatterns = [
        path('player/id/<int:member_number>', views.player_info, name="player_profile"),
        path('players', views.player_list),
        path('player/update/id/<int:member_number>', views.player_update, name="player_update"),
]



