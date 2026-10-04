import math
def bmi(weight, height, units="metric"):
    bmi_value = weight / (height ** 2)

    if units == "imperial":
        bmi_value *= 703

    return bmi_value

def bsa(weight, height, method="mosteller"):
    bsa_value = None
    if method == "mosteller":
        bsa_value = math.sqrt(height * weight / 3600)
    elif method == "dubois":
        bsa_value = 0.007184 * height ** 0.725 * weight ** 0.425
    
    return bsa_value