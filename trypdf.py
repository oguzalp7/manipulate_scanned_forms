from reportlab.pdfgen import canvas
from manipulate-form import name_surname, pre_appointment_employee,pre_appointment_date

filename = f'{name_surname}.pdf'
documentTitle = f"{name_surname}: {pre_appointment_date}: {pre_appointment_employee}"
image = f'{name_surname}.png'
image1 = 'maddeler.png'

pdf = canvas.Canvas(filename, pagesize=(750,2000))

pdf.setTitle(documentTitle)

pdf.drawInlineImage(image, 0, 1050)
pdf.drawInlineImage(image1, 0, 100)

pdf.save()