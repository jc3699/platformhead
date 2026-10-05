# Define the value of C1
c1 = 0.0009367704637676448

# Define the theoretical runtimes
theoretical_runtimes = [
    61438.56189774724,
    132877.1237954945,
    208090.12320405908,
    285754.247590989,
    365241.0118609203,
    446180.24640811817,
    528327.3555562469,
    611508.495181978,
    695593.6821446292,
    780482.0237218406
]

# Calculate the predictive runtimes
predictive_runtimes = [c1 * theoretical_runtime for theoretical_runtime in theoretical_runtimes]

# Print the predictive runtimes
for i, runtime in enumerate(predictive_runtimes, start=1):
    print(f"Predictive Runtime {i}: {runtime}")
