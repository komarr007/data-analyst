
import pandas as pd

def height_preprocess(height_series) -> pd.Series:
    def parse_height(height_str):
        # Split the height string into individual components
        feet, inches = map(int, height_str.split('-'))
        
        # Convert feet and inches to centimeters
        cm = feet * 30.48 + inches * 2.54
        
        return cm

    # Apply the parse_height function to each element in the Series
    cm_height_series = height_series.apply(parse_height)
    
    return cm_height_series

def age_preprocess(birthdate_series, reference_year=2023) -> pd.Series:
    # Convert the birthdate strings to datetime objects, handling different formats
    birthdates = pd.to_datetime(birthdate_series, errors='coerce')

    # Calculate the age based on the specified reference year
    ages = (pd.to_datetime(reference_year, format='%Y') - birthdates) // pd.Timedelta(days=365.25)

    return ages
