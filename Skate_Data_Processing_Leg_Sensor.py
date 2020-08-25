#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

time_of_experiment = {
    "exp1" : "0.19",
    "exp2" : "1.20",
    "exp3" : "2:20",
    "exp4(5)" : "3:07",
    "exp5" : "4:20",
    "exp6(7)" : "5:35",
    "exp7(8)" : "6:30",
    "exp8(9)" : "7:15",
    "exp9(10)" : "7:55",
    "exp10(11)" : "8:35 "
}

URL_keys_skate = {
    "exp2" : '1u2JN_yVS9I-aDDk-xtRFLs9SDdrUNo0f',
    "exp3" : '1qolBHxLSiGi-bmDUZ-V0WzaCay7UaA3x',
    "exp4(5)" : '1eEh3oZpFoCo4dGdcVoGH6kuwIe7QY6rr',
    "exp5" : '1P3E_T65CdJncewSVA-3H8hveejoqcdy4',
    "exp6(7)" : '1kFniM6vHQVy659t0I4R86xH6bfGgo97K',
    "exp7(8)" : '19j6veOIvJoe3aln1MURMChglvMA2F5AS',
    "exp8(9)" : '1akmRWg8bhkKlAQV0XimEPTzsa7_UvazU',
    "exp9(10)" : '1llYUn_deIMOUQl14-aJL9Gw5BqT3nH53',
    "exp10(11)" : '1hdnEeKw7eb2bEvJLbtd12irF3N5qIFmc'
}

URL_keys_Leg = {
    "exp2" : "1jpkzzOPKSsxLzvqVpLwdUXHt7x_zDcQB",
    "exp3" : "19LX_0Se2VrXdYUOwJQ6AJAmw0pG_iapv",
    "exp4(5)" : "1QZ3Kd34F7ozO8-LZ8de__tSvdl9RzSTC",
    "exp5" : "1FvSAAIozBszLYqiX12ms9RBzPSFazGnI",
    "exp6(7)" : "1zs0ss59yLM1xqoOKM5BgZ0b0u-GRln24",
    "exp7(8)" : "1bMeB7DgIvmBkN5g99PVUe1VFHdDDFNqE",
    "exp8(9)" : "1pMKuiQ94n1lzXFSwPEFuVZ2aHYE2vy1-",
    "exp9(10)" : "1Ri5iHWYBIgz8tGcbQKl8oyyJd7YBJJ0h",
    "exp10(11)" : "1X4FWFzKxU47NVt250Gr-X45jjbo8c8Fb"
}

ranges = {
    "exp2" : [4500,5500],
    "exp3" : [4500,6000],
    "exp4(5)" : [4500,5500],
    "exp5" : [4000,5500],
    "exp6(7)" : [4000,5000],
    "exp7(8)" : [3500,5000],
    "exp8(9)" : [4500,6000],
    "exp9(10)" : [3000,4000],
    "exp10(11)" : [6000,7500]
}



n=1

for i in URL_keys_skate:
    google_sheet_ID=URL_keys_Leg[i]
    worksheet_name='Gyroscope'
    path='https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        google_sheet_ID,
        worksheet_name
    )

    data = pd.read_csv(path)

    data.columns = [c.replace(' ', '_') for c in data.columns]
    data.columns = [c.replace('_(rad/s)', '') for c in data.columns]
    data.columns = [c.replace('_(s)', '') for c in data.columns]

    a,b=ranges[i]
    graphdata=data.loc[a:b,:]

    title=i

    plt.subplot(len(URL_keys_skate),1,n)
    #plt.figure(figsize=(15,5))
    plt.plot(graphdata.Time, graphdata.Gyroscope_x, color="red")
    plt.plot(graphdata.Time, graphdata.Gyroscope_y, color="blue")
    plt.plot(graphdata.Time, graphdata.Gyroscope_z, color="green")
    plt.title(title)


    n=n+1


plt.show()
