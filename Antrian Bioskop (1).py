import os
import itertools
import threading
import time
import sys

# -----------------MEMBUAT DATA ANTRIAN----------------- #
class Queue:
    def __init__(self):
        self.size = 5
        self.current_size = 0
        self.data = []

    def kembali(self):
        return self.data[0]

    def front(self):
        return self.data[-1]

    def kosong(self):
        return self.current_size == 0

    def penuh(self):
        return self.current_size == self.size

# -----------------FUNGSI MEMASUKKAN DATA KE ANTRIAN----------------- #
    def enqueue(self, newdata):
        if self.penuh():
            print("\t\t\t\t  Maaf antrian penuh, menambah data", newdata, "tidak dapat dilakukan")
        else:
            self.data.insert(0, newdata)
            self.current_size += 1
            print("\t\t\t\t\t ",newdata, "berhasil dimasukkan dalam antrian")

# -----------------FUNGSI MENGELUARKAN DATA KE ANTRIAN----------------- #
    def dequeue(self):
        self.data.pop(-1)
        print("\n\t\t\t\t\t   Antrian depan sudah keluar")
        self.current_size -= 1

# -----------------FUNGSI CETAK ANTRIAN----------------- #
    def cetak(self):
        print("\n\t\t\t\t\t    Antrian pembelian tiket\n")
        for j in self.data:
            pisah = j.split(",")
            print(('\t[' + pisah[0] + ']').center(10) + "->", end=" ")
        print("[STUDIO]")

# -----------------------------TAMPILAN AWAL----------------------------- #
def menuawal():
    os.system("CLS")
    print("\n\n=======================================================================================================================\n")
    print("\t\t\t\t\t     PROGRAM TIKET BIOSKOP\n")
    print("\t\t\t\t\t\tSELAMAT DATANG")
    print("\n=======================================================================================================================\n")
    input("\t\t\t\t\tTekan (enter) untuk menuju menu")
    film()

# -----------------------------KELUAR PROGRAM----------------------------- #
def keluar():
    done = False

    def animate():
        for i in itertools.cycle(['20%', '45', '75', '100']):
            if done:
                break
            sys.stdout.write('\rLOADING ' + i)
            sys.stdout.flush()
            time.sleep(0.6)
        sys.stdout.write('')

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(2)
    done = True
    os.system("CLS")
    print("ANDA SUDAH KELUAR DARI PROGRAM")

# -----------------------------DAFTRAR FILM----------------------------- #
def film():
    os.system("CLS")
    print("\n\t\t\t\t\t     DAFTAR FILM YANG SEDANG TAYANG")
    print("\t\t\t\t\t\t\t   2023")
    print("=======================================================================================================================\n")
    print("\t\t\t\t\t\t  [1] Fast X\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t  [2] Qodrat\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t  [3] The Little Mermaid\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t  [4] Spiderman\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t  [0] Keluar dari Program\t\t\t\t\t\t\t")
    print("\n=======================================================================================================================\n")
    pf = int(input("\t\t\t\t\t\t   Masukkan Pilihan: "))
    pilihanfilm(pf)

# ------------------------KONDISI PEMILIHAN FILM------------------------ #
def pilihanfilm(pf):
    if pf == 1:
        menu1()
    elif pf == 2:
        menu1()
    elif pf == 3:
        menu1()
    elif pf == 4:
        menu1()
    elif pf == 0:
        print("Keluar dari program")
        keluar()
    else:
        print("\t\t\t\t\t   Masukkan pilihan film yang valid!!")
        input()
        menuawal()

# ------------------------TAMPILAN PEMILIHAN MENU------------------------ #
def menu1():
    os.system("CLS")
    print("\n\t\t\t\t\t          PROGRAM TIKET BIOSKOP")
    print("\t\t\t\t\t\t     SELAMAT DATANG")
    print("=======================================================================================================================\n")
    print("\t\t\t\t\t\t\t  Menu    :\t\t\t\t\t\t\t\n")
    print("\t\t\t\t\t\t1. Melihat daftar antrian\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t2. Menambah antrian\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t3. Menghapus antrian\t\t\t\t\t\t\t")
    print("\t\t\t\t\t\t0. Kembali ke menu\t\t\t\t\t\t\t")
    print("\n=======================================================================================================================\n")
    p1 = int(input("\t\t\t\t\t\t    Masukkan menu   : "))
    pilihan1(p1)

# ------------------------KONDISI PEMILIHAN MENU------------------------ #
def pilihan1(p1):
    if p1 == 1:
        f1satu()
    elif p1 == 2:
        f1dua()
    elif p1 == 3:
        f1tiga()
    elif p1 == 0:
        film()
    else:
        print("\t\t\t\t\t\t  Maaf coba lagi [ENTER]")
        input()
        menu1()

def f1satu():
    os.system("CLS")
    if q1.kosong():
        print("\n\t\t\t\t\t\t+=======================+")
        print("\t\t\t\t\t\t+     Antrian tiket     +")
        print("\t\t\t\t\t\t+=======================+\n")
        print("\t\t\t\t\t\t      Antrian Kosong")
        print("\t\t\t\t\t\t       Tekan [ENTER]")
        input()
        menu1()
    else:
        q1.cetak()
        input()
        menu1()

def f1dua():
    os.system("CLS")
    if q1.penuh():
        print("\n\t\t\t\t\t\t+=======================+")
        print("\t\t\t\t\t\t+     Antrian tiket     +")
        print("\t\t\t\t\t\t+=======================+\n")
        print("\t\t\t\t\t\t   Antrian SUDAH PENUH")
        print("\t\t\t\t\t\t    Tekan [ENTER]")
        input()
        menu1()
    else:
        print("\n\t\t\t\t\t\t+=======================+")
        print("\t\t\t\t\t\t+     Antrian tiket     +")
        print("\t\t\t\t\t\t+=======================+\n")
        data = input("\t\t\t\t\t      Masukkan nama pemesan : ")
        q1.enqueue(data)
        input()
        menu1()

def f1tiga():
    os.system("CLS")
    if q1.kosong():
        print("\n\t\t\t\t\t\t+=======================+")
        print("\t\t\t\t\t\t+     Antrian tiket     +")
        print("\t\t\t\t\t\t+=======================+\n")
        print("\t\t\t\t\t\t      Antrian Penuh")
        print("\t\t\t\t\t\t       Tekan [ENTER]")
        input()
        menu1()
    else:
        q1.dequeue()
        input()
        menu1()

# --------VARIABEL ANTRIAN------- #
q1 = Queue()
q2 = Queue()
q3 = Queue()

# -----MEMANGGIL MENU AWAL----- #
menuawal()

