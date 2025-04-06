# recommendation.py
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def prepare_profile_features(df):
    """Prepare text features for content-based recommendation"""
    # Convert Batch column to string before concatenation
    df['Batch'] = df['Batch'].astype(str)
    
    # Combine relevant fields into a single feature text
    df['features'] = (
        df['State'] + ' ' + 
        df['Category'] + ' ' + 
        df['Eligibility_Caste'] + ' ' + 
        df['Eligibility_Gender'] + ' ' + 
        df['Course_Applicable'] + ' ' + 
        df['Batch']
    )
    return df


def get_personalized_recommendations(df, student_profile, top_n=10):
    """
    Generate personalized scholarship recommendations based on student profile
    
    Parameters:
    -----------
    df : DataFrame
        The scholarship dataset
    student_profile : dict
        Dictionary containing student details like state, course, etc.
    top_n : int
        Number of recommendations to return
        
    Returns:
    --------
    DataFrame with top_n recommended scholarships
    """
    # Prepare dataframe
    df = prepare_profile_features(df)
    
    # Create student profile text
    profile_text = (
        student_profile.get('state', '') + ' ' +
        student_profile.get('category', '') + ' ' +
        student_profile.get('caste', '') + ' ' +
        student_profile.get('gender', '') + ' ' +
        student_profile.get('course', '') + ' ' +
        student_profile.get('batch', '')
    )
    
    # Create a corpus with scholarship features and student profile
    corpus = df['features'].tolist()
    corpus.append(profile_text)  # Add student profile as the last item
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Calculate cosine similarity between student profile and all scholarships
    student_vector = tfidf_matrix[-1]  # Last item is the student profile
    scholarship_vectors = tfidf_matrix[:-1]  # All except the last are scholarships
    
    # Calculate similarities
    similarities = cosine_similarity(student_vector, scholarship_vectors)
    similarities = similarities[0]  # Convert to 1D array
    
    # Get indices of top N similar scholarships
    top_indices = similarities.argsort()[-top_n:][::-1]
    
    # Return top N scholarships
    recommended_scholarships = df.iloc[top_indices].copy()
    recommended_scholarships['similarity_score'] = similarities[top_indices]
    
    return recommended_scholarships[['Scholarship_ID', 'Scholarship_Name', 'Amount', 
                                   'State', 'Category', 'similarity_score']]
