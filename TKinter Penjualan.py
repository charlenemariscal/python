from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox

root = Tk()
root.title('Supermarket')
root.geometry('600x500+100+100')
root.configure(background='light sky blue')

mb = Menubutton(root, text = 'MENU')
mb.menu = Menu(mb)
mb['menu']=mb.menu

def open_window1():
    top = Toplevel()
    top.geometry('600x500+100+100')
    top.title('Penjualan')
    top.configure(background='light sky blue')
    # TANGGAL
    aLabel = ttk.Label(top, text="Pilih Tanggal")
    aLabel.place(bordermode='outside', x=10, y=50)
    v = list(range(1,32))
    tanggalcombo = Combobox(top, values= v)
    tanggalcombo.place(bordermode='outside', x=10, y=80)
    tanggalcombo.set('Pilih Tanggal')
    #BULAN
    bLabel = ttk.Label(top, text="Bulan")
    bLabel.place(bordermode='outside', x=180, y=50)
    w = ['Jan','Feb','Mar','Apr','Mei','Juni','Juli','Agust','Sept','Okt','Nov','Des']
    bulancombo = Combobox(top, values= w)
    bulancombo.place(bordermode='outside', x=180, y=80)
    bulancombo.set('Pilih Bulan')
    #TAHUN
    cLabel = ttk.Label(top, text="Tahun")
    cLabel.place(bordermode='outside', x=350, y=50)
    x = [2017,2018]
    tahuncombo = Combobox(top, values=x)
    tahuncombo.place(bordermode='outside', x=350, y=80)
    tahuncombo.set('Pilih Tahun')

    def lihat():
        f = open('StokPenjualanTkinter.txt')
        data= f.readlines()
        for i in range (len(data)):
            print (data[i])
        f.close()

    savebutton = Button(top,text='Lihat',command = lambda : lihat())
    savebutton.place(bordermode='outside', x=500, y=80)

def open_window2():
    stok = Toplevel()
    stok.geometry('600x500+100+100')
    stok.title('Stok Barang')
    stok.configure(background='light sky blue')

    dlabel = ttk.Label(stok, text = 'EDIT')
    dlabel.place(bordermode = 'outside', x=10,y=10)

    def Tambah_Stok():
        eLabel = ttk.Label(stok, text='Pilih Barang')
        eLabel.place(bordermode='outside', x=20, y=150)
        daft = ['a', 'b', 'c']
        daftar = Combobox(stok, value=daft)
        daftar.place(bordermode='outside', x=200, y=150)
        daftar.set('Pilih Barang')
        fLabel = ttk.Label(stok, text= 'Masukan Jumlah Barang')
        fLabel.place(bordermode = 'outside',x=20, y=200)
        jumlah = IntVar()
        Entryjumlah = Entry(stok, textvariable = jumlah)
        Entryjumlah.place(bordermode = 'outside',x=200, y=200)
        simpanbutton = Button(stok, text = 'Simpan')
        simpanbutton.place(bordermode= 'outside', x=400,y=250)



    def Tambah_Barang():
        eLabel = ttk.Label(stok, text ='Masukan Nama Barang')
        eLabel.place(bordermode = 'outside', x=20,y=150)
        nama = StringVar()
        entrynama = Entry(stok, textvariable = nama)
        entrynama.place(bordermode= 'outside',x= 200,y= 150)
        fLabel = ttk.Label(stok, text='Masukan Jumlah Barang')
        fLabel.place(bordermode='outside', x=20, y=200)
        jumlah = IntVar()
        Entryjumlah = Entry(stok, textvariable=jumlah)
        Entryjumlah.place(bordermode='outside', x=200, y=200)

        def tambah():
            f = open('StokPenjualanTkinter.txt', 'a')
            f.write(nama.get())
            f.write(':')
            f.write(str(jumlah.get()))
            f.write('buah')
            f.close()

        simpanbutton = Button(stok, text='Tambah',command = tambah)
        simpanbutton.place(bordermode='outside', x=400, y=250)

    i = IntVar()
    button = Radiobutton(stok,text = 'Tambah Stok',value=1,variable = i, command = Tambah_Stok)
    button.place(bordermode= 'outside', x=150,y=20)
    button1 = Radiobutton(stok, text = 'Tambah Barang',value=2,variable = i, command = Tambah_Barang)
    button1.place(bordermode='outside', x=350,y=20)

mb.menu.add_command(label = 'Penjualan', command =open_window1)
mb.menu.add_command(label = 'Stok Barang', command =open_window2)
mb.menu.add_command(label= 'Cetak Laporan')
mb.pack()

text = Label(text ='\n\n WELCOME!',background = 'light sky blue',fg = 'palevioletred2', font = 'Arial 50')
text.pack()

mainloop()