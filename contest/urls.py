from django.urls import path

from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.ProporsalView.as_view(), name='create'),
    path('list/', views.ProporsalListView.as_view(), name='list'),
    path('<int:pk>', views.ProporsalDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.ProporsalEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.ProporsalDeleteView.as_view(), name='delete'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
]