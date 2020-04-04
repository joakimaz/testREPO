"""
Aqui, é o mesmo que comentario, mas tudo o que está entre estas quotes é comentario!

A program that stores this book information:
Title
Author
Year
ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete 
Close
"""
#pip install pyinstaller --> para fazer ficheiros executaveis!

#NO FIM: PAra criar o executable file, tenho que no terminal escrever:
# pyinstaller --onefile --windowed DesktopDatabaseApp/FrontEnd.py 
#Sendo que o onefile é para criar so um ficheiro executavel
# windowed para que quando abrir, nao abra com a consola (terminal)
from tkinter import *
import BackEnd #Aqui é para ligar um ao outro, nao ter os dois no mesmo sitio!


def get_selected_row(event): #Aqui serve para ir buscar o id que serve de argumento na funcao delete no backend
    try: #explicado na aula 187
        global selected_tuple #Isto permite que utilize esta variavel fora da funcao, para assim nao ter que passar o valor argumento da funcao
        index= list1.curselection()[0]
        selected_tuple= list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])    
    except IndexError:
        pass
        
        


def view_command():
    list1.delete(0, END) #apaga tudo desde o index 0 até à ultima row, isto, para que sempre que eu pressione o botao view all, ele so mostre uma vez a list!
    for row in BackEnd.viewdata():
        list1.insert(END, row) #As rows novas sao colocadas no fim das rows existentes

def search_command():
    list1.delete(0, END)                #Aqui utilizo o stringvar das entry, pois é onde vou escrever o texto!
    for row in BackEnd.searchdata(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
                                        #O get, é para conseguir que o programa passe o texto para string.
        list1.insert(END, row)

def add_command():
    BackEnd.insertdata(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    BackEnd.deletedata(selected_tuple[0]) #Em vez de utilizar a funcao, so utilizo a variavel global criada!

def update_command():
    BackEnd.updatedata(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    


window= Tk()

window.wm_title("BookDatabase")

label1 = Label(window, text= "Title") #ctrl+ enter e vou para outra linha esteja onde estiver
label1.grid(row=0, column=0)

label2 = Label(window, text="Author")
label2.grid(row=0, column=2)

label3 = Label(window, text="Year")
label3.grid(row=1, column=0)

label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

                        #Se o tipo de texto que eu quiser for string, entao passo stringVAr()
title_text= StringVar() #Mas se eu quisesse que por algum motive fosse uma int por exemplo, entao seria Intvar()
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

author_text= StringVar() 
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

year_text= StringVar()
entry3 = Entry(window, textvariable= year_text)
entry3.grid(row=1, column=1)

isbn_text= StringVar()
entry4 = Entry(window, textvariable= isbn_text)
entry4.grid(row=1, column=3)


button1= Button(window, text="View all", width=12, command=view_command) #funcao acima, feito apos o backend todo!
button1.grid(row=2, column=3)

button2= Button(window, text="Search entry", width=12, command=search_command) #como a funcao no backend recebe parametros, e eu nao posso colocar parametros aqui, tenho que criar a funcao nova!
button2.grid(row=3, column=3)

button3= Button(window, text="Add entry", width=12, command=add_command)
button3.grid(row=4, column=3)

button4= Button(window, text="Update", width=12, command=update_command)
button4.grid(row=5, column=3)

button5= Button(window, text="Delete", width=12, command=delete_command)
button5.grid(row=6, column=3)

button6= Button(window, text="Close", width=12, command= window.destroy)
button6.grid(row=7, column=3)


list1= Listbox(window, height=6, width=35)
list1.grid(row=2, column= 0, rowspan=6, columnspan=2)

list1.bind("<<ListboxSelect>>", get_selected_row)
#Rowspan e columnspan faz com que a lista vá de uma row a outra e column, por exemplo, eu quero que comece na row 2 e que acabe na row 7, entao digo que a rowspan=6
#na columnspan quero que vá do 0 ao 1, daí columnspan=2

scrollbar1= Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)

#Aqui é para ligar a scrollbar À listbox.
list1.configure(yscrollcommand= scrollbar1.set, exportselection=False) #O yscrollcommand é para dizer que o scroll é feito no eixo do y!
scrollbar1.configure(command=list1.yview)



















window.mainloop()