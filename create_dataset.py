# create_dataset.py
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)
fake = Faker('en_IN')  # Indian names ke liye

# Define states and categories
states = ['Andhra Pradesh', 'Assam', 'Bihar', 'Delhi', 'Gujarat', 'Haryana', 
          'Himachal Pradesh', 'Karnataka', 'Kerala', 'Maharashtra', 'Punjab', 
          'Rajasthan', 'Tamil Nadu', 'Telangana', 'Uttar Pradesh', 'West Bengal']

categories = ['Merit-based', 'Need-based', 'Minority', 'Research', 'Sports', 'Women-specific']
eligibility_caste = ['General', 'OBC', 'SC', 'ST', 'All']
eligibility_gender = ['Male', 'Female', 'All']
courses = ['Engineering', 'Medical', 'Arts', 'Science', 'Commerce', 'Any']

def create_scholarship_dataset(num_records=1000):
    """Create a synthetic scholarship dataset"""
    data = []
    
    for _ in range(num_records):
        state = random.choice(states)
        category = random.choice(categories)
        
        # Scholarship name creation
        scholarship_name = f"{random.choice(['National', 'State', 'Private'])} {category} Scholarship for {random.choice(courses)}"
        
        # Different amount ranges based on categories
        if category in ['Research']:
            amount = random.randint(50000, 500000)
        elif category in ['Merit-based', 'Need-based']:
            amount = random.randint(10000, 100000)
        else:
            amount = random.randint(5000, 50000)
        
        # Application dates
        current_date = datetime.now()
        start_date = current_date + timedelta(days=random.randint(-30, 30))
        end_date = start_date + timedelta(days=random.randint(30, 90))
        
        record = {
            'Scholarship_ID': f"SCH{fake.random_number(digits=6)}",
            'Scholarship_Name': scholarship_name,
            'Amount': amount,
            'State': state,
            'Category': category,
            'Batch': random.choice(['2023', '2024', '2025', '2026']),
            'Eligibility_Caste': random.choice(eligibility_caste),
            'Eligibility_Gender': random.choice(eligibility_gender),
            'Min_Percentage_Required': random.randint(50, 95),
            'Course_Applicable': random.choice(courses),
            'Application_Start_Date': start_date.strftime('%Y-%m-%d'),
            'Application_Deadline': end_date.strftime('%Y-%m-%d'),
            'Contact_Email': f"contact@{state.lower().replace(' ', '')}scholarships.gov.in"
        }
        data.append(record)
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Create dataset
    df = create_scholarship_dataset(1000)
    
    # Save to CSV
    df.to_csv('scholarship_dataset.csv', index=False)
    print(f"Dataset created with 1000 scholarships and saved as 'scholarship_dataset.csv'")
    
    # Show sample
    print("\nSample data:")
    print(df.head())
