# filter_functions.py
import pandas as pd
from datetime import datetime

def load_dataset(file_path='scholarship_dataset.csv'):
    """Load the scholarship dataset from CSV"""
    return pd.read_csv(file_path)

def filter_by_state(df, states=None):
    """Filter scholarships by state(s)"""
    if not states or 'All' in states:
        return df
    return df[df['State'].isin(states)]

def filter_by_caste(df, castes=None):
    """Filter scholarships by caste eligibility"""
    if not castes or 'All' in castes:
        return df
    # Include scholarships marked as 'All' and those matching specified castes
    return df[(df['Eligibility_Caste'].isin(castes)) | (df['Eligibility_Caste'] == 'All')]

def filter_by_gender(df, gender=None):
    """Filter scholarships by gender eligibility"""
    if not gender or gender == 'All':
        return df
    # Include scholarships marked as 'All' and those matching specified gender
    return df[(df['Eligibility_Gender'] == gender) | (df['Eligibility_Gender'] == 'All')]

def filter_by_amount(df, min_amount=0, max_amount=None):
    """Filter scholarships by amount range"""
    if max_amount:
        return df[(df['Amount'] >= min_amount) & (df['Amount'] <= max_amount)]
    return df[df['Amount'] >= min_amount]

def filter_by_batch(df, batches=None):
    """Filter scholarships by applicable batch years"""
    if not batches:
        return df
    return df[df['Batch'].isin(batches)]

def filter_by_category(df, categories=None):
    """Filter scholarships by category"""
    if not categories:
        return df
    return df[df['Category'].isin(categories)]

def filter_by_course(df, courses=None):
    """Filter scholarships by applicable courses"""
    if not courses:
        return df
    # Include scholarships marked as 'Any' and those matching specified courses
    return df[(df['Course_Applicable'].isin(courses)) | (df['Course_Applicable'] == 'Any')]

def filter_by_percentage(df, min_percentage=0):
    """Filter scholarships by minimum required percentage"""
    return df[df['Min_Percentage_Required'] <= min_percentage]

def filter_active_scholarships(df):
    """Filter currently active scholarships (application date not passed)"""
    today = datetime.now().strftime('%Y-%m-%d')
    return df[df['Application_Deadline'] >= today]

def apply_all_filters(df, states=None, castes=None, gender=None, 
                     min_amount=0, max_amount=None, batches=None,
                     categories=None, courses=None, min_percentage=0,
                     active_only=False):
    """Apply all filters sequentially"""
    filtered_df = df.copy()
    
    filtered_df = filter_by_state(filtered_df, states)
    filtered_df = filter_by_caste(filtered_df, castes)
    filtered_df = filter_by_gender(filtered_df, gender)
    filtered_df = filter_by_amount(filtered_df, min_amount, max_amount)
    filtered_df = filter_by_batch(filtered_df, batches)
    filtered_df = filter_by_category(filtered_df, categories)
    filtered_df = filter_by_course(filtered_df, courses)
    filtered_df = filter_by_percentage(filtered_df, min_percentage)
    
    if active_only:
        filtered_df = filter_active_scholarships(filtered_df)
    
    return filtered_df

