from reportlab.pdfgen import canvas
import os
from celery import shared_task

@shared_task
def create_pdf_invoice_task(booking_id, booking_date, package_id, user_id, price, package_destination):    
    c = canvas.Canvas(f"Booking No{booking_id}.pdf")
    c.drawString(100, 750, 'Booking No:{}'.format(booking_id))
    c.drawString(100, 700, 'Issue Date:{}'.format(booking_date))
    c.drawString(100, 680, 'Billed To:{}'.format(user_id))
    c.drawString(100, 660, 'Product Description:')
    c.drawString(150, 640, 'Product ID:{}'.format(package_id))
    c.drawString(150, 620, 'Trip Destination:{}'.format(package_destination))
    c.drawString(100, 600, 'Total Amount: {} $'.format(price))
    c.save()