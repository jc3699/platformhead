theoretical_rts = [
    61438.5618977472,
    132877.123795495,
    208090.123204059,
    285754.247590989,
    365241.01186092,
    446180.246408118,
    528327.355556247,
    611508.495181978,
    695593.682144629,
    780482.023721841
]

# Define list of empirical response times (from previous response)
empirical_rts = [
    45.7120656967163,
    103.518557548523,
    168.027377128601,
    241.177582740784,
    306.515622138977,
    392.534565925598,
    472.861957550049,
    558.572173118591,
    616.22793674469,
    731.132507324219
]

# Calculate the ratios for each pair of empirical and theoretical response times
ratios = [empirical / theoretical for empirical, theoretical in zip(empirical_rts, theoretical_rts)]

# Print the ratios
for i, ratio in enumerate(ratios, start=1):
    print(f"Ratio for empirical RT {i}: {ratio}")