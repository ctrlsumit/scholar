# app.py
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Import our modules
from filter_functions import *
from visualizations import *
from recommendation import *

class ScholarshipFilterSystem:
    def __init__(self, data_path='scholarship_dataset.csv'):
        """Initialize the system with dataset"""
        print("Initializing Scholarship Filter System...")
        self.df = pd.read_csv(data_path)
        self.filtered_df = self.df.copy()
        print(f"Loaded {len(self.df)} scholarships from dataset")
        
    def display_stats(self):
        """Display basic statistics about the dataset"""
        print("\n=== SCHOLARSHIP DATASET STATISTICS ===")
        print(f"Total Scholarships: {len(self.df)}")
        print(f"States Covered: {len(self.df['State'].unique())}")
        print(f"Scholarship Categories: {', '.join(sorted(self.df['Category'].unique()))}")
        print(f"Amount Range: ₹{self.df['Amount'].min()} to ₹{self.df['Amount'].max()}")
        print(f"Average Scholarship Amount: ₹{int(self.df['Amount'].mean())}")
        
        # Count active scholarships
        today = datetime.now().strftime('%Y-%m-%d')
        active_count = len(self.df[self.df['Application_Deadline'] >= today])
        print(f"Active Scholarships: {active_count}")
        
    def apply_filters(self, **filter_kwargs):
        """Apply selected filters to the dataset"""
        self.filtered_df = apply_all_filters(self.df, **filter_kwargs)
        return self.filtered_df
    
    def visualize_data(self):
        """Generate visualizations for filtered data"""
        if len(self.filtered_df) == 0:
            print("No data to visualize! Please apply filters first.")
            return
            
        print(f"Generating visualizations for {len(self.filtered_df)} scholarships...")
        # Create output directory if it doesn't exist
        os.makedirs('visualizations', exist_ok=True)
        
        # Generate all visualizations
        generate_all_visualizations(self.filtered_df)
        
    def get_recommendations(self, student_profile, top_n=10):
        """Get personalized scholarship recommendations"""
        results = get_personalized_recommendations(self.df, student_profile, top_n)
        return results
        
    def export_results(self, filename='filtered_scholarships.csv'):
        """Export filtered results to CSV"""
        if len(self.filtered_df) == 0:
            print("No data to export! Please apply filters first.")
            return
            
        self.filtered_df.to_csv(filename, index=False)
        print(f"Exported {len(self.filtered_df)} scholarships to {filename}")
        
if __name__ == "__main__":
    # Example usage
    system = ScholarshipFilterSystem()
    system.display_stats()
    
    # Example: Apply state and caste filters
    filtered = system.apply_filters(
        states=['Maharashtra', 'Delhi'],
        castes=['OBC', 'All'],
        min_amount=10000,
        active_only=True
    )
    
    print(f"\nFound {len(filtered)} matching scholarships")
    print(filtered[['Scholarship_Name', 'Amount', 'State']].head())
    
    # Example: Get personalized recommendations
    student = {
        'state': 'Maharashtra',
        'course': 'Engineering',
        'caste': 'OBC',
        'gender': 'Male',
        'batch': '2024'
    }
    
    recommendations = system.get_recommendations(student, top_n=5)
    print("\nTop personalized scholarship recommendations:")
    print(recommendations)
    
    # Generate visualizations and export
    system.visualize_data()
    system.export_results()
