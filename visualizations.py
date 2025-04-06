# visualizations.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def set_styling():
    """Set consistent styling for all visualizations"""
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    
def plot_scholarship_distribution_by_state(df):
    """Plot bar chart of scholarships by state"""
    set_styling()
    plt.figure(figsize=(14, 8))
    
    state_counts = df['State'].value_counts()
    sns.barplot(x=state_counts.index, y=state_counts.values, palette='viridis')
    
    plt.title('Distribution of Scholarships by State', fontsize=16)
    plt.xlabel('State', fontsize=14)
    plt.ylabel('Number of Scholarships', fontsize=14)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('scholarships_by_state.png')
    plt.show()

def plot_scholarship_amount_distribution(df):
    """Plot distribution of scholarship amounts"""
    set_styling()
    
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Amount'], bins=20, kde=True)
    plt.title('Distribution of Scholarship Amounts', fontsize=16)
    plt.xlabel('Amount (₹)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.tight_layout()
    plt.savefig('scholarship_amounts.png')
    plt.show()
    
    # Box plot by category
    plt.figure(figsize=(14, 8))
    sns.boxplot(x='Category', y='Amount', data=df, palette='Set3')
    plt.title('Scholarship Amounts by Category', fontsize=16)
    plt.xlabel('Category', fontsize=14)
    plt.ylabel('Amount (₹)', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('amounts_by_category.png')
    plt.show()

def plot_eligibility_breakdown(df):
    """Plot pie charts for caste and gender eligibility"""
    set_styling()
    
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Caste eligibility pie chart
    caste_counts = df['Eligibility_Caste'].value_counts()
    ax1.pie(caste_counts, labels=caste_counts.index, autopct='%1.1f%%', 
            startangle=90, colors=sns.color_palette('Set3', len(caste_counts)))
    ax1.set_title('Scholarships by Caste Eligibility', fontsize=16)
    
    # Gender eligibility pie chart
    gender_counts = df['Eligibility_Gender'].value_counts()
    ax2.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', 
            startangle=90, colors=sns.color_palette('pastel', len(gender_counts)))
    ax2.set_title('Scholarships by Gender Eligibility', fontsize=16)
    
    plt.tight_layout()
    plt.savefig('eligibility_breakdown.png')
    plt.show()

def plot_batch_course_heatmap(df):
    """Plot heatmap of scholarships by batch and course"""
    set_styling()
    
    # Create crosstab
    heatmap_data = pd.crosstab(df['Batch'], df['Course_Applicable'])
    
    plt.figure(figsize=(14, 10))
    sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', fmt='d', linewidths=.5)
    plt.title('Scholarships Available by Batch and Course', fontsize=16)
    plt.tight_layout()
    plt.savefig('batch_course_heatmap.png')
    plt.show()

def generate_all_visualizations(df):
    """Generate all visualizations for dataset"""
    plot_scholarship_distribution_by_state(df)
    plot_scholarship_amount_distribution(df)
    plot_eligibility_breakdown(df)
    plot_batch_course_heatmap(df)
    
    print("All visualizations have been generated and saved!")
