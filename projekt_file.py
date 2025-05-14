### Projekt FMSF50 Matematisk statistik Maj 2025

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import norm, gumbel_r
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





# Load data from CSV files
lulealven_data = pd.read_csv('luleälven_årsmax.csv')['maxflöde'].values  # Adjust 'Flow' to match your column name
vindelalven_data = pd.read_csv('vindelälven_årsmax.csv')['maxflöde'].values  # Adjust 'Flow' to match your column name

# Combine datasets for analysis
all_data = np.concatenate([lulealven_data, vindelalven_data])
datasets = {'Luleälven': lulealven_data, 'Vindelälven': vindelalven_data}

# Function to fit distributions and calculate parameters
def fit_distributions(data):
    # Fit normal distribution
    norm_params = norm.fit(data)
    norm_ks, norm_p = stats.kstest(data, 'norm', args=norm_params)

    # Fit Gumbel distribution (right-skewed, common for maxima)
    gumbel_params = gumbel_r.fit(data)
    gumbel_ks, gumbel_p = stats.kstest(data, 'gumbel_r', args=gumbel_params)

    return {
        'Normal': {'params': norm_params, 'ks_stat': norm_ks, 'p_value': norm_p},
        'Gumbel': {'params': gumbel_params, 'ks_stat': gumbel_ks, 'p_value': gumbel_p}
    }

# Analyze each dataset
results = {}
for name, data in datasets.items():
    results[name] = fit_distributions(data)

# Check if same distribution fits all datasets (simplified comparison using p-value threshold of 0.05)
same_dist = all(r['Gumbel']['p_value'] > 0.05 or r['Normal']['p_value'] > 0.05 for r in results.values())

# Create overview table
table_data = []
for name, dist_results in results.items():
    for dist, res in dist_results.items():
        table_data.append([name, dist, res['params'], res['ks_stat'], res['p_value']])

df_results = pd.DataFrame(table_data, columns=['River', 'Distribution', 'Parameters', 'KS Statistic', 'P-value'])

# Print table
print("Overview of Distribution Fitting")
print(df_results.to_string(index=False))
print(f"\nSame distribution type fits all datasets: {same_dist}")

# Optional: Plot histograms with fitted distributions
for name, data in datasets.items():
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=10, density=True, alpha=0.6, color='g', label='Data')
    
    # Plot Normal fit
    x = np.linspace(min(data), max(data), 100)
    plt.plot(x, norm.pdf(x, *results[name]['Normal']['params']), 'r-', lw=2, label='Normal Fit')
    
    # Plot Gumbel fit
    plt.plot(x, gumbel_r.pdf(x, *results[name]['Gumbel']['params']), 'b-', lw=2, label='Gumbel Fit')
    
    plt.title(f'{name} Annual Maxima Distribution Fit')
    plt.xlabel('Flow (m³/s)')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{name}_distribution_fit.png')
    plt.close()


