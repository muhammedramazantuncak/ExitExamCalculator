from tkinter import *

# window oluşturma

def window_maker(window_title,color,x,y):
    window_ex = Tk()
    window_ex.title(window_title)
    window_ex["bg"] = color
    window_ex.minsize(x,y)
    return window_ex

window = window_maker("ÖSYM EXAM LEAVİNG TİME","orange",600,600)

# Font oluşturma

def font_maker():
    font_ex = ("Courier",10,"bold")
    return font_ex

# yerleştirme oluşturma

def relx_rely(example,x,y):
    example.place(relx=x,rely=y,anchor="center")

# Label oluşturma

def label_maker(text,x,y):
    label_ex = Label()
    label_ex.config(text=text,bg="orange",fg="black",font=font_maker())
    relx_rely(label_ex,x,y)

label_maker("Please enter only the hour part of your exam entry time",0.5,0.1)
label_maker("Please enter only the minute part of your exam entry time",0.5,0.25)
label_maker("Please enter only the hour part of your exam finishing time",0.5,0.4)
label_maker("Please enter only the minute part of your exam finishing time",0.5,0.55)

# entry oluşturma

def entry_maker(x,y):
    entry_ex = Entry(width=50)
    relx_rely(entry_ex,x,y)
    return entry_ex

h_starting_time = entry_maker(0.5,0.15)
m_starting_time = entry_maker(0.5,0.3)
h_finishing_time = entry_maker(0.5,0.45)
m_finishing_time = entry_maker(0.5,0.6)

# entry alma

def get_entries(example):
    return example.get()

# print label oluşturma

printing_label : Label | None = None

def print_label(text):
    global printing_label
    hide_func()
    printing_label = Label()
    printing_label.config(text=text, bg="orange", fg="black", font=font_maker())
    relx_rely(printing_label,0.5,0.8)

# hide fuoknsşyonu oluşturma

def hide_func():
    global printing_label
    if printing_label is not None:
        printing_label.place_forget()

# click fonksiyonu oluşturma

def click_func():
    global h_starting_time,h_finishing_time,m_finishing_time,m_starting_time
    constant_minute = 60
    constant_percentage = 0.75
    constant_minus = 15
    h_s_t = get_entries(h_starting_time)
    h_f_t = get_entries(h_finishing_time)
    m_s_t = get_entries(m_starting_time)
    m_f_t = get_entries(m_finishing_time)
    try:
        if not h_s_t or not h_f_t or not m_s_t or not m_f_t:
            print_label("Please do not leave the relevant fields blank !!!")
        elif int(h_s_t) > int(h_f_t):
            print_label("Please be careful while filling the fields which are relevant to hour !!!")
        elif len(h_s_t) >= 3 or len(h_f_t) >= 3 or len(m_f_t) >= 3 or len(m_s_t) >= 3:
            print_label("Please give attention to filling the fields in a logical manner !!!")
        elif True:
            total_time = ((int(h_f_t)-int(h_s_t))*constant_minute) + (int(m_f_t)-int(m_s_t))
            h_early_exit_time = int(h_s_t) + ((total_time*constant_percentage)//constant_minute)
            m_early_exit_time = int(m_s_t) + ((total_time*constant_percentage)%constant_minute)
            h_end_exit_time = int(h_s_t) + ((total_time-constant_minus)//constant_minute)
            m_end_exit_time = int(m_s_t) + ((total_time-constant_minus)%constant_minute)
            print_label(f"Your exam is starting at {int(h_s_t)}.{m_s_t}\nYour exam is finishing at {int(h_f_t)}.{m_f_t}\nYou can leave the exam from {int(h_early_exit_time)}.{int(m_early_exit_time)} until {h_end_exit_time}.{m_end_exit_time}")
    except ValueError:
        print_label("Please fill the fields only using numbers !!!")


def button_maker():
    button_ex = Button()
    button_ex.config(text="Calculate",width=50,command=click_func)
    relx_rely(button_ex,0.5,0.7)

button_maker()






















window.mainloop()