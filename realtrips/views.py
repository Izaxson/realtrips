from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from realtrips.models import Expense, Trip
from django.views.generic import ListView  ,DetailView , CreateView ,FormView ,UpdateView
from django.db.models import Sum
from django.contrib import messages
from .forms import  TripAddForm ,ExpenseAddForm ,EditTripForm



# def addtrip(request):
#     form = TripForm()
#     # trip_total_collection= Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum'] 
#     context = {'form': form}
#     return render(request, 'realtrips/addtrip.html', context)


class TripListView(ListView):
    model = Trip
    
    trip_total_collection= Trip.objects.aggregate(Sum('amount_collected'))['amount_collected__sum'] 
    context = {'TotalAmount':trip_total_collection }
    template_name = 'realtrips/trips.html' # name of your home template

  
    # paginate_by=5
    

class DashboardView(ListView):
    model= Trip
    template_name = 'realtrips/dashboard.html' # name of your home template


class ExpenseListView(ListView):
    model = Expense
    template_name = 'realtrips/expense.html' # name of your home template
    # paginate_by=10   


class TripAddView(FormView):
    template_name = 'realtrips/addtrip.html'
    form_class = TripAddForm  # corrected
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
    # form_class = EditTripForm
    success_url = reverse_lazy('trips')
    
    def form_valid(self, form):
        form.save()
        
        # messages.success(self.request, 'Your Trip has been updated. Thank you!')
        # return super().form_valid(form)
        
    def get_queryset(self):
        # Return a queryset of all Trip objects
        return Trip.objects.all()
            
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


# class EditExpenseView(UpdateView):
#     template_name = 'realtrips/update_expense.html'
#     form_class = ExpenseEditForm
#     success_url = reverse_lazy('expense')
    
#     def form_valid(self, form):
#         form.save()
        
#         messages.success(self.request, 'Your Expense  has been updated. Thank you!')
#         return super().form_valid(form)
        
#     def get_queryset(self):
#         # Return a queryset of all Expense objects
#         return Expense.objects.all()  