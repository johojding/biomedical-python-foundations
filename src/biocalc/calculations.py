import math

def bmi(weight, height):
    _validate_nums(weight, "weight")
    _validate_nums(height, "height")
    bmi_value = weight / (height ** 2)
    return bmi_value

def bsa(weight, height, method="mosteller"):
    _validate_nums(weight, "weight")
    _validate_nums(height, "height")
    _validate_str(method, "method")
    
    if method.lower() == "mosteller":
        bsa_value = math.sqrt(height * weight / 3600)
    elif method.lower() == "dubois":
        bsa_value = 0.007184 * height ** 0.725 * weight ** 0.425
    else:
        raise ValueError("Method must be either 'mosteller' or 'dubois'.")
    return bsa_value

def zscore(data_point, mean, std):
    _validate_nums(data_point, "data point", pos=False)
    _validate_nums(mean, "mean", pos=False)
    _validate_nums(std, "STD")
    score = (data_point - mean) / std
    return score

def si_unit_conversion(value, unit):
    _validate_nums(value, "input value")
    _validate_str(unit, "unit")
    if unit.lower() == "inch":
        return value * 0.0254
    elif unit.lower() == "foot":
        return value * 0.3048
    elif unit.lower() == "lbs":
        return value * 0.45359237
    elif unit.lower() == "g":
        return value * 0.001
    elif unit.lower() == "cm":
        return value * 0.01
    else:
        raise ValueError("Conversion of that unit does not exist in the function.")

def bmi_range(bmi_value):
    _validate_nums(bmi_value, "BMI value")
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value <= 24.9:
        return "normal"
    elif bmi_value <= 29.9:
        return "overweight"
    else:
        return "obese"

def bsa_range(bsa_value):
    _validate_nums(bsa_value, "BSA value")
    if bsa_value < 1.5:
        return "low"
    elif bsa_value < 2.0:
        return "normal"
    else:
        return "high"

def _validate_nums(value, name, pos=True):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be input as int or float.")
    if pos:
        if value <= 0:
            raise ValueError(f"{name} must be positive.")

def _validate_str(s, name):
    if not isinstance(s, str):
        raise TypeError(f"{name} must be str.")