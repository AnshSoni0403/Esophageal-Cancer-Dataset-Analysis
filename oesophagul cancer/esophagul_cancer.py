# -*- coding: utf-8 -*-
"""esophagul cancer

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jr1ieqE1kgnrAGOnZ_vlKySC77hvgQiF
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

input_file = r"C:\Users\ANSH\Downloads\oesophagul cancer\Esophageal_Dataset.csv"
df = pd.read_csv(input_file)
print(df.head())

"""DATA **CLEANING**"""

df.fillna(0, inplace=True)

"""*Total people suffering from this disease*"""

df['patient_barcode'].count()

"""*location of tissue where cancer is detected higher*"""

tissue_count = df.groupby('tissue_source_site')['patient_barcode'].count()
print(tissue_count)

# Create the plot
plt.figure(figsize=(12, 6))
plt.bar(tissue_count.index, tissue_count.values, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Patient Counts per Tissue Source Site', fontsize=16)
plt.xlabel('Tissue Source Site', fontsize=14)
plt.ylabel('Patient Count', fontsize=14)

# Rotate x-ticks for readability if there are many categories
plt.xticks(rotation=45, ha='right')

# Add gridlines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()



# Calculate age by dividing 'days_to_birth' by 365 and taking the absolute value
df['age'] = (df['days_to_birth'] / -365).round().astype(int)  # Rounding for whole years and converting to integer

"""*Age wise - which age group is more prone to this cancer*"""

# Group data by age and count occurrences
age_distribution = df['age'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(age_distribution.index, age_distribution.values, color='skyblue')
plt.xlabel('Age')
plt.ylabel('Cancer Count')
plt.title('Age-wise Distribution of Cancer Cases')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

"""The age-wise cancer case distribution shows a peak in individuals aged 50-80, with the highest cases around 60-70. This indicates that cancer risk rises with age, especially after 50, and drops after 80. The low incidence in younger groups suggests age-targeted screening programs are crucial, particularly for those in their 60s and 70s, to improve early detection and intervention.

*Gender Wise Distribution*
"""

gender_distribution = df['gender'].value_counts()

# Plotting as a pie chart
plt.figure(figsize=(8, 8))
plt.pie(gender_distribution.values, labels=gender_distribution.index, autopct='%1.1f%%', colors=['skyblue', 'salmon'], startangle=140)
plt.title("Gender Distribution of Cancer Cases")
plt.show()

"""Males have higher risk of this by approx 70% more times

*BMI Analysis*
"""

# Convert height from centimeters to meters
df['Height_m'] = df['height'] / 100

# Calculate BMI using the correct formula
df['BMI'] = df['weight'] / (df['Height_m'] ** 2)

plt.figure(figsize=(8, 6))
sns.boxplot(x='BMI', data=df, color="lightcoral")
plt.title("Box Plot of BMI")
plt.xlabel("BMI")
plt.show()

"""The box plot highlights that individuals with higher BMI levels, especially those falling into the outlier range (above 40), may face an increased risk of esophageal cancer. This suggests that improper or elevated BMI could be a significant factor in cancer susceptibility, emphasizing the importance of maintaining a healthy BMI to potentially reduce cancer risk.

*Country of Procurement*
"""

colors = [
    'skyblue', 'salmon', 'lightgreen', 'orange', 'purple', 'pink', 'yellow', 'lightcoral',
    'lightseagreen', 'plum', 'gold', 'deepskyblue', 'coral', 'lightpink', 'khaki', 'lightblue',
    'mediumpurple', 'turquoise', 'lavender', 'tan', 'lightyellow', 'teal', 'orchid', 'peru',
    'steelblue', 'thistle', 'indianred', 'seashell', 'lightcyan', 'bisque', 'peachpuff'
]

# Data for the pie chart
country = df['country_of_procurement'].value_counts()

# Plotting the pie chart with more colors
plt.pie(country.values, labels=country.index, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Country of Procurement")
plt.show()

"""The higher prevalence of esophageal cancer cases in the United States and Vietnam, as indicated by the larger segments in the pie chart, may be due to several factors:

1. **Diet and Lifestyle**:
   - **United States**: Diets high in processed foods, red meat, and sugary drinks can increase the risk of esophageal cancer. Obesity, which is common in the U.S., is also a major risk factor. Additionally, high rates of smoking and alcohol consumption contribute to the risk.
   - **Vietnam**: In Vietnam, diets may include certain types of preserved or pickled foods, which contain carcinogenic substances. Smoking is also prevalent among Vietnamese men, and alcohol consumption is a common cultural practice, both of which increase cancer risk.

2. **Environmental Factors**:
   - **United States**: High levels of pollution in some areas and exposure to certain industrial chemicals may contribute to cancer risk. Additionally, urban environments often encourage sedentary lifestyles, leading to obesity-related risks.
   - **Vietnam**: Vietnam faces challenges with air pollution and exposure to pesticides and other chemicals in agriculture. These environmental factors may play a role in increasing cancer incidence.

3. **Healthcare Accessibility and Screening**:
   - **United States**: While healthcare is accessible, the high cost may lead to delayed diagnoses for some individuals, increasing the severity of cases when discovered.
   - **Vietnam**: Limited access to early screening and preventive healthcare services in rural areas may lead to late-stage diagnoses, worsening outcomes.

These factors combined likely contribute to the observed higher rates of esophageal cancer in these countries.

*Dead & Alive Status*
"""

live_status = df['vital_status'].value_counts()

# Plotting the pie chart
plt.pie(live_status.values, labels=live_status.index, autopct='%1.1f%%', colors=['skyblue', 'salmon'], startangle=140)
plt.title("Live Status")
plt.show()

"""More prone to death."""

# Group by 'city_of_procurement' and calculate the normalized counts of 'vital_status'
city_death = df.groupby('city_of_procurement')['vital_status'].value_counts(normalize=True).unstack()

# Define a color palette for better visualization
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#9b59b6', '#34495e']

# Plotting the bar plot with increased figure width and adjusted bar width
plt.figure(figsize=(20, 90))  # Larger width for better readability
city_death.plot(kind='bar', stacked=True, color=colors[:len(city_death.columns)], width=0.5, edgecolor='black')
plt.title("Proportion of Vital Status by City of Procurement", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("City of Procurement", fontsize=14, labelpad=15)
plt.ylabel("Proportion", fontsize=14, labelpad=15)
plt.legend(title='Vital Status', loc='upper right', fontsize=12, title_fontsize=13, framealpha=0.9)  # Slightly less transparent legend
plt.xticks(rotation=45, ha='center', fontsize=11)  # Center align labels for readability
plt.yticks(fontsize=11)
plt.tight_layout(pad=3)  # Adjusts padding to fit everything well
plt.show()

"""*Smoking and it's effect*"""

## Get the sorted value counts of ages when smoking began
smoking = df['age_began_smoking_in_years'].value_counts().sort_index()

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(smoking.index, smoking.values, marker='o', color='b', linestyle='-', linewidth=2)
plt.title("Age When Smoking Began")
plt.xlabel("Age Began Smoking (Years)")
plt.ylabel("Number of People suffering cancer")
plt.grid(True)
plt.show()

"""This highlights that people who start smoking at a very young age i.e <10 years have a veryy high risk of cancer

*Alcohol Consumption*
"""

# Assuming df is your DataFrame containing 'amount_of_alcohol_consumption_per_day' and 'vital_status'
# Create the box plot with interchanged axes
plt.figure(figsize=(10, 6))
sns.boxplot(x='vital_status', y='amount_of_alcohol_consumption_per_day', data=df)
plt.title('Boxplot of Vital Status vs Alcohol Consumption')
plt.xlabel('Vital Status')
plt.ylabel('Amount of Alcohol Consumption per Day')
plt.show()

"""The boxplot suggests a potential link between alcohol consumption and vital status. The median alcohol consumption for deceased individuals appears lower than for those alive. However, significant overlap exists, indicating alcohol consumption alone isn't a definitive predictor. Other factors likely influence health outcomes."""