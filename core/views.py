from django.shortcuts import render
import datetime
from django.conf import settings
from twilio.rest import Client
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
        
        # Send message via Twilio
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                from_=settings.TWILIO_WHATSAPP_NUMBER,
                body=message_body,
                to=settings.TARGET_WHATSAPP_NUMBER
            )
            return render(request, 'core/index.html', {'success': True})
        except Exception as e:
            error_msg = f"Error sending WhatsApp message: {str(e)}"
            print(error_msg)
            return render(request, 'core/index.html', {'success': False, 'error': error_msg})
            
    return render(request, 'core/index.html')
