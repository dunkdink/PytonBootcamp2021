#GUITranslator.py

from tkinter import *
#จากไลยรารี tkinter * คือดึงความสามารถหลักมาทั้งหมด

from tkinter import ttk # ttk is theme of tk
#------Google Translate-------
from googletrans import Translator
translator = Translator()
#----สร้างหน้ัาต่างหลัก----
GUI = Tk()
GUI.geometry('500x300')# ก x ส
GUI.title('วุ้นแปลภาษา')
#----Config----
FONT = ('Angsana New',15)
#----Label----
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()
#---------Entry(ช่องกรอกข้อความ)--------
v_vocab = StringVar() #กล่องเก็บข้อความ
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)
#---------Botton(Translate)--------
def Translate():
    vocab = v_vocab.get() #.get คือให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print(vocab + ' : ' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text)

B1 = ttk.Button(GUI,text='Translate',command=Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx= 20,ipady=5) #show ปุ่มจากบนลงล่าง

#----Label----
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()

#----Result----
v_result = StringVar()
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2,foreground='green')
R1.pack()



GUI.mainloop() #โปรแกรมรันได้ตลอดเวลา(บรรทัดสุดท้ายเท่านั้น)




