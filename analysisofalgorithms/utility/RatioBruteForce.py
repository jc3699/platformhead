# Theoretical response times
theoretical_rts = [
    25000000,
    100000000,
    225000000,
    400000000,
    625000000,
    900000000,
    1225000000,
    1600000000,
    2025000000,
    2500000000
]

# Empirical response times in milliseconds
empirical_rts = [
    2213.55636119843,
    10389.9547576904,
    22239.4123315811,
    41185.7044458389,
    61747.12870121,
    88033.3647966385,
    120343.229699135,
    161869.900751114,
    198686.630582809,
    250146.617007256,
]

# Calculate the ratios for each pair of empirical and theoretical response times
ratios = [empirical / theoretical for empirical, theoretical in zip(empirical_rts, theoretical_rts)]

# Print the ratios
for i, ratio in enumerate(ratios, start=1):
    print(f"{ratio:.15f},")