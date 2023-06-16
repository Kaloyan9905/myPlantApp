from django.urls import path, include

from myPlantApp.web.views import index, catalogue, create_profile, details_profile, edit_profile, delete_profile, \
    create_plant, details_plant, edit_plant, delete_plant

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),

    path('create/', create_plant, name='create plant'),
    path('details/<int:plant_id>/', details_plant, name='details plant'),
    path('edit/<int:plant_id>/', edit_plant, name='edit plant'),
    path('delete/<int:plant_id>/', delete_plant, name='delete plant'),

    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)
