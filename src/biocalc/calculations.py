import math
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    return bmi_value

def bsa(weight, height, method="mosteller"):
    if method == "mosteller":
        bsa_value = math.sqrt(height * weight / 3600)
    elif method == "dubois":
        bsa_value = 0.007184 * height ** 0.725 * weight ** 0.425
    else:
        return
    return bsa_value

def zscore(data_point, mean, std):
    score = (data_point - mean) / std
    return score

def si_unit_conversion(value, unit):
    if unit == "inch":
        return value * 0.0254
    elif unit == "foot":
        return value * 0.3048
    elif unit == "lbs":
        return value * 0.45359237
    elif unit == "g":
        return value * 0.001
    elif unit == "cm":
        return value * 0.01
    return

def bmi_range(bmi_value):
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value <= 24.9:
        return "normal"
    elif bmi_value <= 29.9:
        return "overweight"
    else:
        return "obese"

def bsa_range(bsa_value):
    if bsa_value < 1.5:
        return "low"
    elif bsa_value < 2.0:
        return "normal"
    else:
        return "high"