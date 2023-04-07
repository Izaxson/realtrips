from django import views
from django.urls import include, path


# from Vehicles import settings
from .views import   EditTripView, ExpenseAddView, TripDetailView, TripAddView, TripListView , ExpenseListView , DashboardView
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
      
    path('', DashboardView.as_view(), name='dashboard'),
    path('trips/', TripListView.as_view(), name='trips'),
    path('addtrip/', TripAddView.as_view(), name='addtrip'),
    path('edittrip/<str:pk>', EditTripView.as_view(), name='edit-trip'),
    path('viewtrip/<str:pk>', TripDetailView.as_view(), name='viewtrip'),

   
    path('expense/', ExpenseListView.as_view(), name='expense'),
    path('addexpense/', ExpenseAddView.as_view(), name='addexpense'),
    # path('editexpense/<str:pk>', EditExpenseView.as_view(), name='edit-expense'),
    # path('viewexpense/<str:pk>', TripDetailView.as_view(), name='viewtrip'),
 ]
