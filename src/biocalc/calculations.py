import math

def bmi(weight, height):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be input as int or float.")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be input as int or float.")
    if weight <= 0 or height <= 0:
        raise ValueError("Height and weight must be positive numbers.")
    bmi_value = weight / (height ** 2)
    return bmi_value

def bsa(weight, height, method="mosteller"):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be input as int or float.")
    if not isinstance(height, (int, float)):
         raise TypeError("Height must be input as int or float.")
    if weight <= 0 or height <= 0:
         raise ValueError("Height and weight must be positive numbers.")
    if not isinstance(method, str):
        raise TypeError("Method must be str.")
    
    if method.lower() == "mosteller":
        bsa_value = math.sqrt(height * weight / 3600)
    elif method.lower() == "dubois":
        bsa_value = 0.007184 * height ** 0.725 * weight ** 0.425
    else:
        raise ValueError("Method must be either 'mosteller' or 'dubois'.")
    return bsa_value

def zscore(data_point, mean, std):
    if not isinstance(data_point, (int, float)):
        raise TypeError("Input point must be int or float.")
    if not isinstance(mean, (int, float)):
        raise TypeError("Mean must be int or float.")
    if not isinstance(std, (int, float)):
        raise TypeError("STD must be int or float.")
    if std <= 0:
        raise ValueError("STD must be a positive number.")
    score = (data_point - mean) / std
    return score

def si_unit_conversion(value, unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Input value must be int or float.")
    if not isinstance(unit, str):
        raise TypeError("Unit must be str.")
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
    if not isinstance(bmi_value, (int, float)):
        raise TypeError("Input value must be int or float.")
    if bmi_value <= 0:
        raise ValueError("Input value must be a positive number.")
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value <= 24.9:
        return "normal"
    elif bmi_value <= 29.9:
        return "overweight"
    else:
        return "obese"

def bsa_range(bsa_value):
    if not isinstance(bsa_value, (int, float)):
        raise TypeError("Input value must be int or float.")
    if bsa_value <= 0:
        raise ValueError("Input value must be a positive number.")
    if bsa_value < 1.5:
        return "low"
    elif bsa_value < 2.0:
        return "normal"
    else:
        return "high"