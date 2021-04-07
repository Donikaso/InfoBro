from colorama import *
import datetime
import requests
from bs4 import BeautifulSoup as BS
from tkinter import *

init()
keyword = ("курс доллара")
url_rub = (f'https://www.google.com/search?q={keyword}&num=50&&hl=en')
url_corona = ("https://стопкоронавирус.рф")

HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

today = datetime.date.today()
now = today.strftime("%B %d, %Y")

response1 = requests.get(url_rub, headers=HEADERS)
response2 = requests.get(url_corona, headers=HEADERS)

soup1 = BS(response1.content, 'html.parser')
soup2 = BS(response2.content, 'html.parser')


def f_one():
    sum_ill = soup2.find_all(class_='cv-countdown__item-value _accent')
    print("\n" + Fore.BLUE, now, Style.RESET_ALL)
    print("Всего заболевших: " + Fore.RED, sum_ill[0].text, Style.RESET_ALL)
    print("Заболевших в России за день: " + Fore.RED, sum_ill[1].text, Style.RESET_ALL)
    print()


def second_f():
    print(Fore.GREEN, "\n1.Wash your hands\n2.Put on a mask"
                      "\n3.Don't touch your face in street\n4.Sit at home\n", Style.RESET_ALL)


def f_three():
    course = soup1.find(class_="DFlfde SwHCTb")
    print(Fore.BLUE, now, Style.RESET_ALL)
    print(Fore.GREEN, '1$ = ' + Fore.RED, course.text + '₽', Style.RESET_ALL)
    print()


def f_four():
    print(Fore.YELLOW, "\n1.Одержимость\n2.Пазманский дьявол\n3.Паразиты\n"
                       "4.Зелёная миля\n5.Иван Васильевич меняет проффессию\n", Style.RESET_ALL)


tk = Tk()
tk.title("InfoBro")
tk.configure(bg='#4766B8')
tk.geometry("601x350")
tk.resizable(False, False)

b1 = Button(tk, width='22', height='5', background='#868483', foreground='#E03E3E', activebackground='#868483',
            activeforeground='#E03E3E',
            text="Numbers of sick coronavirus", command=f_one).place(x=9, y=109)

b2 = Button(tk, width='22', height='5', background='#868483', foreground='#FF4836', activebackground='#868483',
            activeforeground='#FF4836',
            text="Soviets vs coronavirus", command=second_f).place(x=9, y=231)

b3 = Button(tk, width='22', height='5', background='#868483', foreground='#8DC7EB', activebackground='#868483',
            activeforeground='#8DC7EB',
            text="Dollar rate", command=f_three).place(x=430, y=109)

b4 = Button(tk, width='22', height='5', background='#868483', foreground='#8DC7EB', activebackground='#868483',
            activeforeground='#8DC7EB',
            text="Good films", command=f_four).place(x=430, y=231)

tk.mainloop()