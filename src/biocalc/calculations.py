
def bmi(weight, height, units="metric"):
    bmi_value = weight / (height ** 2)

    if units == "imperial":
        bmi_value *= 703

    return bmi_value