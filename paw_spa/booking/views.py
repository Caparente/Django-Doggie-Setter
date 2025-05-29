from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking 
from .forms import BookingForm
from django.contrib import messages  # For flash messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Home page
def home(request):
    return render(request, 'home.html')

# Booking form
def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been booked successfully!')
            return redirect('book')  # Redirects to the same form page after submission
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

# View all bookings
def view_bookings(request):
    bookings = Booking.objects.all().order_by('-date')  # newest first
    return render(request, 'view_bookings.html', {'bookings': bookings})

# Delete a booking
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view_bookings')

# Admin Login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error_message': 'Invalid credentials or insufficient permissions.'})
    
    return render(request, 'admin_login.html')

# Admin Logout
@login_required
def admin_logout(request):
    logout(request)
    return redirect('home')

# Admin Dashboard
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Access Denied")
    
    status_filter = request.GET.get('status', 'all')
    
    if status_filter == 'all':
        bookings = Booking.objects.all().order_by('-date')
    else:
        bookings = Booking.objects.filter(status=status_filter).order_by('-date')
    
    context = {
        'bookings': bookings,
        'status': status_filter
    }
    
    return render(request, 'admin_dashboard.html', context)

# Update Booking Status
@login_required
def update_booking_status(request, booking_id, new_status):
    if not request.user.is_staff:
        return HttpResponseForbidden("Access Denied")
    
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=booking_id)
        if new_status in ['approved', 'declined']:
            booking.status = new_status
            booking.save()
            messages.success(request, f'Booking #{booking_id} has been {new_status}.')
        
    return redirect('admin_dashboard')




