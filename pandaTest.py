import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dati/meteo_Bari.csv')

df.head()
a = plt.hist(df['temperature_2m'], bins=50)
print(a)
occorrenza_massimo = a[0].argmax()
valore_massimo = a[1][occorrenza_massimo]

max_perc = 0.9
concurrent_per = 0
dx=0
sx=0
while(concurrent_per<max_perc):

    if a[0][occorrenza_massimo+dx+1]>a[0][occorrenza_massimo-sx-1]:
        dx+=1
        sum_par = a[0][occorrenza_massimo-sx:occorrenza_massimo+dx].sum()
        sum_tot = a[0].sum()
        concurrent_per = sum_par/sum_tot

    else:
        sx += 1
        sum_par = a[0][occorrenza_massimo - sx:occorrenza_massimo + dx].sum()
        sum_tot = a[0].sum()
        concurrent_per = sum_par / sum_tot


## Estremo sinistro
print(occorrenza_massimo - sx)
## Estremo destro
print(occorrenza_massimo + dx)

