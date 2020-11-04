import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Price_Indices.csv")

plt.figure(figsize=(12,6))

def f0():
    plt.bar(df["KAYIT SIRA"],df["EN YUKSEK"], color = "green")
    plt.xlabel("Endex Kayıt Sırası")
    plt.ylabel("En Yüksek Endex Değeri")
    plt.title("BIST Pay Endeksleri Grafiği")
    plt.show()

def f1():
    plt.bar(df["KAYIT SIRA"],df["EN DUSUK"], color = "green")
    plt.xlabel("Endex Kayıt Sırası")
    plt.ylabel("En Düşük Endex Değeri")
    plt.title("BIST Pay Endeksleri Grafiği")
    plt.show()

def f2():
    plt.bar(df["KAYIT SIRA"],df["ACILIS"], color = "green")
    plt.xlabel("Endex Kayıt Sırası")
    plt.ylabel("Açılış Endex Değeri")
    plt.title("BIST Pay Endeksleri Grafiği")
    plt.show()

def f3():
    plt.bar(df["KAYIT SIRA"],df["KAPANIS"], color = "green")
    plt.xlabel("Endex Kayıt Sırası")
    plt.ylabel("Kapanış Endex Değeri")
    plt.title("BIST Pay Endeksleri Grafiği")
    plt.show()

def f4(operation):
    if(operation == 1): f0()
    elif(operation == 2): f1()
    elif(operation == 3): f2()
    elif(operation == 4): f3()
    else: print("Geçersiz İşlem Girdisi"); f5()

def f5():
    print("BIST Pay Endeksleri Grafik Oluşturucuya Hoşgeldiniz")
    print("En Yüksek Endex Değeri-Endex Kayıt Sırası Grafiği(1)")
    print("En Düşük Endex Değeri-Endex Kayıt Sırası Grafiği(2)")
    print("Açılış Endex Değeri-Endex Kayıt Sırası Grafiği(3)")
    print("Kapanış Endex Değeri-Endex Kayıt Sırası Grafiği(4)")
    operation = int(input("Lütfen yapılacak işlemi seçin : "))
    f4(operation)

f5()
