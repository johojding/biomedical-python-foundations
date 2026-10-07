# Biomedical Python Foundations

## Project description
Biomedical Python Foundations is an educational Python project containing reusable functions for common biomedical calculations. The project demonstrates basic Python package development, input validation, automated testing with pytest, and usage of a package through a small synthetic-data example.

The package currently provides functions for:
* Body mass index (BMI)
* Body surface area (BSA)
* Z-score calculation 
* Conversion of selected units to SI units
* BMI reference range classification
* BSA reference range classification

All example patient and laboratory data used in this project are synthetic.

## Installation

### Requirements
- Python: >=3.14
- Python virtual environment using venv

### Used for development/testing
- Git: 2.56.0.windows.1
- VS Code: 1.140.0
- pytest: 9.1.1

### Setup
Clone repository and navigate into the project directory.
Create a virtual environment:
    `python -m venv .venv`
Activate the virtual environment:
    `.\.venv\Scripts\Activate`
Install the package in editable mode:
    `python -m pip install -e .`
Install pytest:
    `python -m pip install pytest`

## Usage
The functions can be imported directly from the biocalc package:
    `from biocalc import bmi, bsa, zscore, si_unit_conversion, bmi_range, bsa_range`

For examples on how to use functions, see `demo.py` under `examples` or run `python.\examples\demo.py`

## Testing
The project uses pytest for automated testing.
Run all tests from the project root:
    `pytest`

The test suite covers normal calculations, invalid inputs, and boundary cases for the package functions.

## Assumptions and limitations

### Units
* `bmi()` expects weight in kilograms and height in metres.
* `bsa()` expects weight in kilograms and height in centimetres.
* `si_unit_conversion()` converts the supported input units to SI units.

### Supported BSA methods
The `bsa()` function currently supports the following methods:
* Mosteller
* Du Bois

An unsupported method raises `ValueError`.

### Input validation
The functions perform basic runtime validation. Inputs with inappropriate types raise `TypeError`, while values that are not valid for calculation raise `ValueError`.

### Reference ranges
The BMI and BSA classification functions use simplified reference ranges implemented for this project. These ranges should not be interpreted as universal clinical guidelines or used as a substitute for professional medical assessment.