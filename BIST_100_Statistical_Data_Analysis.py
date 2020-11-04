import pandas as pd

df = pd.read_csv("Price_Indices.csv")

print("\n BIST Pay Endeksleri Tablosu \n")

print(df)

print("\n Veri Seti Boyutu : "+str(df.shape[0])+" Satır "+str(df.shape[1])+" Sütun \n")

print("\n Sayısal Verileri İstatiksel Analiz Tablosu \n")

print(df.describe())

print("\n En Yüksek ve En Düşük Pay Endesklerine Sıralama Tablosu \n")

print(df.sort_values(by="EN YUKSEK", ascending=False).head(10))

print("\n Endeks Kodu ve En Yüksek Pay Endesklerinin Ortalamaları Tablosu \n")

print(df.groupby("ENDEKS KODU")["EN YUKSEK"].mean())

print("\n Endeks Kodu ve En Düşük Pay Endesklerinin Ortalamaları Tablosu \n")

print(df.groupby("ENDEKS KODU")["EN DUSUK"].mean())


    
