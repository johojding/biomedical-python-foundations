from biocalc.calculations import bmi, bsa, zscore, si_unit_conversion, bmi_range, bsa_range

# Patient data
weight = 65     #kg  
height = 175    #cm

# Synthetic lab data
data_point = 278
mean = 254
std = 12

# Calculations
height_in_m = si_unit_conversion(height, "cm")
patient_bmi = bmi(weight, height_in_m)
patient_bsa = bsa(weight, height, method="dubois")



print("Synthetic patient example")
print(f"BMI: {patient_bmi:.2f}")
print(f"BSA: {patient_bsa:.2f}")
print(f"BMI category: {bmi_range(patient_bmi)}")
print(f"BSA category: {bsa_range(patient_bsa)}")

print()
print("Synthetic lab measurement")
print(f"New data point: {data_point}")
print(f"Mean: {mean}")
print(f"STD: {std}")
print(f"Z-score: {zscore(data_point, mean, std):.2f}")
