from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from realtrips.models import Expense, Trip,Driver
from django.views.generic import ListView  ,DetailView , CreateView ,FormView ,UpdateView
from django.db.models import Sum
from django.contrib import messages
from .forms import  ExpenseEditForm, TripAddForm ,ExpenseAddForm ,EditTripForm
from django.contrib.auth.decorators import login_required, permission_required





class TripListView(ListView):
    model = Trip
    template_name = 'realtrips/trips.html' # name of your home template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate mileage for each trip
        trips = context['object_list']
        for trip in trips:
            trip.mileage = trip.odometer_close - trip.odometer_start

        return context


class DashboardView(ListView):
    model= Trip
    template_name = 'realtrips/dashboard.html' # name of your home template
    def total_amount_collected(self):
        return Trip.objects.aggregate(Sum('amount_collected'))['amount_collected_sum']

    def form_valid(self, form):
        form.save()

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Trip.objects.all()
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate the total amount collected
        total_amount_collected = Trip.objects.aggregate(Sum('amount_collected')).get('amount_collected__sum')
        context['total_amount_collected'] = total_amount_collected
            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred

         # Calculate the Net revenue
        net_revenue = total_amount_collected - total_expense_incurred
        context['net_revenue'] = net_revenue

        # Calculate trip count
        context['trip_count'] = Trip.objects.all().count()
        # Calculate mileage
        context['mileage'] = Trip.objects.aggregate(mileage=Sum('odometer_close') - Sum('odometer_start'))
        # Calculate trip total collection
        context['trip_total_collection'] = Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum']
        return context

class ExpenseListView(ListView):
    model = Expense
    template_name = 'realtrips/expense.html' # name of your home template

    paginate_by=10


class TripAddView(FormView):
    template_name = 'realtrips/addtrip.html'
    form_class = TripAddForm  
    success_url = reverse_lazy('trips')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'Your Trip has been added. Thank you!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.form_class()
        return context

class EditTripView(UpdateView):
    template_name = 'realtrips/update_trip.html'
    form_class = EditTripForm
    success_url = reverse_lazy('trips')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'Your Trip has been updated. Thank you!')
        return super().form_valid(form)

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Trip.objects.all()

class TripDetailView(DetailView):
    template_name = 'realtrips/viewtrip.html'
    success_url = reverse_lazy('viewtrip')

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Trip.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # driver = Driver.objects.get(vehicle__vehicle_reg_no='vehicle_reg_no')
        # driver_name = driver.name
        # context['driver'] = driver
        return context
class RevenueListView(ListView):
    template_name = 'realtrips/revenue_report.html'
    # template_name = 'realtrips/expense_report.html'
    success_url = reverse_lazy('trip')

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Expense.objects.all()
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred

        return context



    def total_amount_collected(self):
        return Trip.objects.aggregate(Sum('amount_collected'))['amount_collected_sum']

    def form_valid(self, form):
        form.save()

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Trip.objects.all()
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate the total amount collected
        total_amount_collected = Trip.objects.aggregate(Sum('amount_collected')).get('amount_collected__sum')
        context['total_amount_collected'] = total_amount_collected
            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred

         # Calculate the Net revenue
        net_revenue = total_amount_collected - total_expense_incurred
        context['net_revenue'] = net_revenue
        return context

class ExpenseReportListView(ListView):
    template_name = 'realtrips/report-expense.html'
    success_url = reverse_lazy('report-expense')

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Expense.objects.all()
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred

        return context

    def get_queryset(self):
        # Return a queryset of all Trip objects
         return Expense.objects.all()
    # paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

            # Calculate the total expenses
        total_expense_incurred = Expense.objects.aggregate(Sum('amount_incurred')).get('amount_incurred__sum')
        context['total_expense_incurred'] = total_expense_incurred
        return context

class ExpenseAddView(FormView):
    template_name = 'realtrips/addexpense.html'
    form_class = ExpenseAddForm
    success_url = reverse_lazy('expense')

    def form_valid(self, form):
        form.save()

        messages.success(self.request, 'Your Expense  has been added. Thank you!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.form_class()
        return context

class EditExpenseView(UpdateView):
    form_class = ExpenseEditForm
    template_name = 'realtrips/update_expense.html'
    success_url = reverse_lazy('expense')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your Expense  has been updated. Thank you!')
        return super().form_valid(form)

    def get_queryset(self):
        # Return a queryset of all Expense objects
        return Expense.objects.all()

class ExpenseDetailView(DetailView):
    template_name = 'realtrips/viewexpense.html'
    success_url = reverse_lazy('trips')

    # def form_valid(self, form):
    #     form.save()

    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Expense.objects.all()
        # return Expense.objects.filter(pk=expenser.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calculate total amount incurred
        total_expense_amount = Expense.objects.aggregate(Sum('amount_incurred'))['amount_incurred__sum']
        context['totalexpense_amount'] = total_expense_amount

        # total_trip_amount = Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum']
        # context['totaltrip_amount'] = total_trip_amount


        return context
