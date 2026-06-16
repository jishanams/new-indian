from django.shortcuts import render, redirect
import datetime
import urllib.parse
from django.conf import settings
from .models import Booking

def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        model = request.POST.get('model')
        reg = request.POST.get('reg')
        stype = request.POST.get('stype')
        date_str = request.POST.get('date')
        notes = request.POST.get('notes')
        
        # Parse date or use today as fallback
        try:
            date_val = datetime.datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else datetime.date.today()
        except ValueError:
            date_val = datetime.date.today()
            
        booking = Booking.objects.create(
            name=name or "Not provided",
            phone=phone or "Not provided",
            vehicle_model=model or "Not provided",
            registration_no=reg or "",
            service_type=stype or "Not provided",
            preferred_date=date_val,
            notes=notes or ""
        )
        
        # Format message for WhatsApp
        message_body = (
            f"*New Service Booking*\n"
            f"Name: {booking.name}\n"
            f"Phone: {booking.phone}\n"
            f"Vehicle: {booking.vehicle_model}\n"
            f"Reg No: {booking.registration_no}\n"
            f"Service: {booking.service_type}\n"
            f"Date: {booking.preferred_date}\n"
            f"Notes: {booking.notes}"
        )
        
        # URL encode the message
        encoded_message = urllib.parse.quote(message_body)
        
        # Extract the number from settings (e.g., 'whatsapp:+919847554297' -> '919847554297')
        # Fallback to the website's default number if setting is missing
        target_number = "918075856132"
        if hasattr(settings, 'TARGET_WHATSAPP_NUMBER') and settings.TARGET_WHATSAPP_NUMBER:
            target_number = settings.TARGET_WHATSAPP_NUMBER.replace('whatsapp:+', '').replace('+', '')
            
        whatsapp_url = f"https://wa.me/{target_number}?text={encoded_message}"
        
        # Redirect the user to WhatsApp
        return redirect(whatsapp_url)
            
    return render(request, 'core/index.html')
