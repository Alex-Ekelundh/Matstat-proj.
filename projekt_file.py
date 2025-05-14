### Projekt FMSF50 Matematisk statistik Maj 2025

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pandas as pd

luledf = pd.read_csv("luleälven_årsmax.csv")
vindeldf = pd.read_csv("vindelälven_årsmax.csv")

"""
Fråga 1: Jämför grafiskt hur årsmaximum varierar under de olika perioderna för respektive älv.
Presentera en översiktstabell med antal observationer, medelvärde, standardavvikelse, minimum 
och maximum i de fyra fallen
"""

# Luleå: P1 = 1901-1939, P2 = 1980-2022
# Vindel: P1 = 1911-1939, P2 = 1980-2022
luledfP1 = luledf[luledf["år"] <= 1939]
luledfP2= luledf[luledf["år"] > 1939]

vindeldfP1 = vindeldf[vindeldf["år"] <= 1939]
vindeldfP2 = vindeldf[vindeldf["år"] > 1939]

luledata1 = {
    "obsv" : luledfP1["maxflöde"].count(),
    "medel" :luledfP1["maxflöde"].mean(),
    "stddev" : luledfP1["maxflöde"].std(),
    "max" : luledfP1["maxflöde"].max(),
    "min" : luledfP1["maxflöde"].min()
}
 
luledata2 = {
    "obsv" : luledfP2["maxflöde"].count(),
    "medel" :luledfP2["maxflöde"].mean(),
    "stddev" : luledfP2["maxflöde"].std(),
    "max" : luledfP2["maxflöde"].max(),
    "min" : luledfP2["maxflöde"].min()
}

vindeldata1 = {
    "obsv" : vindeldfP1["maxflöde"].count(),
    "medel" :vindeldfP1["maxflöde"].mean(),
    "stddev" : vindeldfP1["maxflöde"].std(),
    "max" : vindeldfP1["maxflöde"].max(),
    "min" : vindeldfP1["maxflöde"].min()
}

vindeldata2 = {
    "obsv" : vindeldfP2["maxflöde"].count(),
    "medel" :vindeldfP2["maxflöde"].mean(),
    "stddev" : vindeldfP2["maxflöde"].std(),
    "max" : vindeldfP2["maxflöde"].max(),
    "min" : vindeldfP2["maxflöde"].min()
}

summary = pd.DataFrame.from_dict({
    "Luleå P1 (1901–1939)": luledata1,
    "Luleå P2 (1980–2022)": luledata2,
    "Vindel P1 (1911–1939)": vindeldata1,
    "Vindel P2 (1980–2022)": vindeldata2
}, orient="index")

print(type(summary))
summary = summary[["obsv", "medel", "stddev", "min", "max"]]

print(summary.to_string())


plt.figure(figsize=(10, 6))


plt.plot(luledfP1['år'],   luledfP1['maxflöde'],   label='Luleå P1 (1901–1939)')
plt.plot(luledfP2['år'],   luledfP2['maxflöde'],   label='Luleå P2 (1980–2022)')
plt.plot(vindeldfP1['år'], vindeldfP1['maxflöde'], label='Vindel P1 (1911–1939)')
plt.plot(vindeldfP2['år'], vindeldfP2['maxflöde'], label='Vindel P2 (1980–2022)')

plt.xlabel('År')
plt.ylabel('Maxflöde')
plt.title('Årsmaximum för Luleälven & Vindelälven')
plt.legend()
plt.tight_layout()
plt.show()


