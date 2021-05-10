import pandas as pd
import os
import numpy as np

indir = './'

if not os.path.exists(indir+'/processed'):
    os.makedirs(indir+'/processed')

list405 = []
list460 = []
list405_460 = []
list460_405 = []
listpH = []
titles = []
times_min = []

#pH calibration curve
Bottom = 0.03596
Top = 4.180
HillSlope = 0.9763
LogIC50 = 7.838


filelist = sorted(os.listdir('%s/' %indir))

for f in filelist:
    if f.endswith('csv'):
        print(indir+f)
        df = pd.read_csv(indir+f, skiprows = 1)

        ex405 = df.iloc[:,1]
        ex405 = pd.to_numeric(ex405, errors='coerce').dropna()
        list405.append(ex405)

        ex460 = df.iloc[:,3]
        ex460 = pd.to_numeric(ex460, errors='coerce').dropna()
        list460.append(ex460)

        rat405_460 = ex405/ex460
        rat405_460 = pd.to_numeric(rat405_460, errors='coerce').dropna()
        list405_460.append(rat405_460)

        rat460_405 = ex460/ex405
        rat460_405 = pd.to_numeric(rat460_405, errors='coerce').dropna()
        list460_405.append(rat460_405)

        pH = -(np.log10((1/rat460_405)*(Bottom + (Top - Bottom)) - 1)/HillSlope - LogIC50)
        pH = pd.to_numeric(pH, errors='coerce').dropna()
        listpH.append(pH)

        times_min.append(pd.to_numeric(df.iloc[:,0], errors='coerce').dropna())
        titles.append(f[:-4])


times_min = pd.concat(times_min, axis = 1).dropna(axis=1)
times_sec = times_min*60
df405_460 = pd.concat(list405_460, axis = 1)
df405_460.columns = titles
df405_460 = pd.concat((times_sec,df405_460), axis = 1)
df405_460 = df405_460.rename(columns={'Time (min)': 'Time (sec)'})
df405_460.to_csv(indir+'/processed/processed_405-460.csv')

df460_405 = pd.concat(list460_405, axis = 1)
df460_405.columns = titles
df460_405 = pd.concat((times_sec,df460_405), axis = 1)
df460_405 = df460_405.rename(columns={'Time (min)': 'Time (sec)'})
df460_405.to_csv(indir+'/processed/processed_460-405.csv')

df405 = pd.concat(list405, axis = 1)
df405.columns = titles
df405 = pd.concat((times_sec,df405), axis = 1)
df405 = df405.rename(columns={'Time (min)': 'Time (sec)'})
df405.to_csv(indir+'/processed/processed_405.csv')

df460 = pd.concat(list460, axis = 1)
df460.columns = titles
df460 = pd.concat((times_sec,df460), axis = 1)
df460 = df460.rename(columns={'Time (min)': 'Time (sec)'})
df460.to_csv(indir+'/processed/processed_460.csv')

dfpH = pd.concat(listpH, axis = 1)
dfpH.columns = titles
dfpH = pd.concat((times_sec,dfpH), axis = 1)
dfpH = dfpH.rename(columns={'Time (min)': 'Time (sec)'})
dfpH.to_csv(indir+'/processed/processed_pH.csv')
