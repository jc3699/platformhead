# Theoretical runtime values
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

# Multiplying each theoretical runtime value by the factor 0.00010054819276928875
predicted_rts = [0.000103899547577 * rt for rt in theoretical_rts]

# Print the predicted runtime values
for i, predicted_rt in enumerate(predicted_rts, start=1):
    print(f"Predicted runtime for Theoretical RT {i}: {predicted_rt}")