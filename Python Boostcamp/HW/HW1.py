# HW1.py
"""โจทย์การบ้าน #HW1 : สร้างโปรแกรมคำนวณโดยใช้ GUI (Tkinter) มีช่องกรอกอย่างน้อย 3 ช่อง หลังจากคำนวณแล้วให้โชว์ผลลัพธ์หน้า GUI 
เช่น โปรแกรมคำนวณสินค้า + vat 7% 
ช่องกรอกที่ E1: ชื่อสินค้า
ช่องกรอกที่ E2: ราคา
ช่องกรอกที่ E3: จำนวน
calculate = E2 * E3 + 7% 
คำนวณเสร็จโชว์ผลลัพธ์หน้า GUI """

from tkinter import *
from tkinter import ttk

# ----สร้างหน้ัาต่างหลัก----
GUI = Tk()
GUI.geometry('500x400')
GUI.title('โปรแกรมคำนวณสินค้า + vat 7% ')

FONT = ('Angsana New', 15)

# ----Label----

L1 = ttk.Label(GUI, text='ชื่อสินค้า', font=FONT)
L2 = ttk.Label(GUI, text='ราคา', font=FONT)
L3 = ttk.Label(GUI, text='จำนวน', font=FONT)

# ---------Entry(ช่องกรอกข้อความ)--------
v_product = StringVar()
v_price = StringVar()
v_amount = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_product, font=FONT, width=40)
E2 = ttk.Entry(GUI, textvariable=v_price, font=FONT, width=40)
E3 = ttk.Entry(GUI, textvariable=v_amount, font=FONT, width=40)

# ----เรียงลำดับ----
L1.pack(pady=5)
E1.pack(pady=5)
L2.pack(pady=5)
E2.pack(pady=5)
L3.pack(pady=5)
E3.pack(pady=5)
# ---------Botton(calculate)--------


def Calculate():
    product = v_product.get()
    price = int(v_price.get())
    amount = int(v_amount.get())
    total = price * amount
    vat7 = total * (7/107)
    nettotal = total * (100/107)

    print('ราคาก่อน vat:{:.2f}(vat7%:{:.2f})'.format(nettotal, vat7))
    v_result.set('สินค้า{} จำนวน{}ชิ้น ราคารวมภาษี{:.2f}บาท (Vat7%{:.2f}บาท)'.format(product,amount,nettotal,vat7))


B1 = ttk.Button(GUI, text='Calculate', command=Calculate)
B1.pack(ipadx=20, ipady=10)

# ผลลัพท์จากการคำนวณ
v_result = StringVar()
v_result.set('ผลลัพท์โชว์จุดนี้')

R1 = ttk.Label(GUI, textvariable=v_result, font=FONT)
R1.pack()


GUI.mainloop()
