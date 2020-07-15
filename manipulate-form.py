import cv2
from reportlab.pdfgen import canvas
import time

font = cv2.FONT_HERSHEY_SIMPLEX
color = (0, 0, 0)
text = "test"
mark = '+'
wedding_coords = (350, 460)
engage_coords = (350, 505)
kina_coords = (350, 550)
save_date_coords = (350, 590)
special_event_coords = (350, 680)
img = cv2.imread("studio-form.png", 1)

name_surname = input("ad-soyad giriniz: ")
deposit = input("Kapora giriniz: ")
pre_appointment_date = input("gorusme tarihi giriniz: ")
pre_appointment_employee = input("gorusme yapilan calisani giriniz: ")
pref_artist = input("talep edilen artist belirtiniz: ")
print("konsept secimi icin girisler: (dugun, nisan, kina, dis cekim, ozel gun) gibi giriniz. ")
concept = input("konsept seçimi: ")
extra_guest = input("gelin+ sayisi: ")
total = input("toplam ödenecek miktarı giriniz: ")
desc = input("aciklama giriniz: ")

h = img.shape[0]
w = img.shape[1]

cv2.putText(img, name_surname, (350, 240), font, 1, color, 2) #add name_surname
cv2.putText(img, deposit, (350, 280), font, 1, color, 2) #deposit
cv2.putText(img, pre_appointment_date, (350, 330), font, 1, color, 2) #pre appointment date
cv2.putText(img, pre_appointment_employee, (350, 370), font, 1, color, 2) #pre appointment employee
cv2.putText(img, extra_guest, (350, 635), font, 1, color, 2) #extra guests
cv2.putText(img, total, (350, 725), font, 1, color, 2) #total
cv2.putText(img,pref_artist, (470, 420), font, 1, color, 2) #pref_artist
cv2.putText(img, desc, (250, 790), font, 1, color, 2) #desc


if concept == 'dugun':
    cv2.putText(img, mark, wedding_coords, font, 1, color, 2)
elif concept == 'nisan':
    cv2.putText(img, mark, engage_coords, font, 1, color, 2)
elif concept == 'kina':
    cv2.putText(img, mark, kina_coords, font, 1, color, 2)
elif concept == 'dis cekim':
    cv2.putText(img, mark, save_date_coords, font, 1, color, 2)
elif concept == 'ozel gun':
    cv2.putText(img, mark, special_event_coords, font, 1, color, 2)
else:
    print("konsept ismi girişiniz hatalıdır.")

cv2.imwrite(f"{name_surname}.png",img)




