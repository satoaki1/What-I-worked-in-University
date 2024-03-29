# -*- coding: utf-8 -*-
"""ITS69304_Group1_Asgn_SectionC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nXkKihgfhwKwFRrdxn85knXoFW80liP9
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("student-mat.csv")

df

"""### Question 1"""

df.info()

df.columns

"""### Question 2"""

# Determine the total number of attributes within the dataset
print(f"Total number of attributes within the dataset is {len(df.columns)}")

"""### Question 3"""

# Assess the dataset's dimensions to identify both the number of rows and columns
print(f"The dataset has {df.shape[0]} rows with {df.shape[1]} columns")

"""### Question 4"""

# Calculate the average values for "Dalc," "Walc," and "days of absences,"
# rounding these figures to two decimal places for precision
Dalc_avg = round(df["Dalc"].mean(), 2)
Walc_avg = round(df["Walc"].mean(), 2)
doa_avg = round(df["absences"].mean(), 2)

print(f"The average of Dalc is: {Dalc_avg}")
print(f"The average of Walc is: {Walc_avg}")
print(f"The average of days of absences is: {doa_avg}")

"""### Question 5"""

# Finding both the minimum and maximum values of "days of absences"
doa_min = df["absences"].min()
doa_max = df["absences"].max()

print(f"The minimum value of days of absences is {doa_min}")
print(f"The maximum value of days of absences is {doa_max}")

"""### Question 6"""

# Calculate the correlation between these two attributes to quantify their relationship
dtoa_corr = df["Dalc"].corr(df["absences"])
atod_corr = df["absences"].corr(df["Dalc"])

print(f"The correlation between Dalc and days of absences is {round(dtoa_corr, 4)}")
print(f"The correlation between days of absences and Dalc is {round(atod_corr, 4)}")

# Visualize this correlation using a heatmap
sns.heatmap(df[["Dalc", "absences"]].corr(), annot = True)
plt.show()

"""### Question 7

#### **Question (a)**
"""

# The range of days for absences observed in the dataset
doa_min = df["absences"].min()
doa_max = df["absences"].max()

print(f"The minimum value of days of absences is {doa_min}.")
print(f"The maximum value of days of absences is {doa_max}.")
print(f"Therefore, the days of absences ranges from {doa_min} to {doa_max}, gap is {doa_max - doa_min}.")

"""#### **Question (b)**"""

# Identify the most and least frequent days for absences among students
doa_freqs = df["absences"].value_counts()

print(f"The most frequent days of absences is {doa_freqs.idxmax()} with frequency of {doa_freqs.max()}.")
print(f"The most frequent days of absences is {doa_freqs.idxmin()} with frequency of {doa_freqs.min()}.")

"""#### **Question (c)**"""

# Create a histogram to visualize the distribution of days for absences
sns.histplot(df["absences"], kde = True)
plt.show()

"""#### **Question (d)**"""

# Apply linear regression function from scipy into the dataset to see the relationship
slope, intercept, r_value, p_value, std_err = linregress(df["Dalc"], df["absences"])

# Calculate the R-squared value to observe the experiment performance
r2_score = round(r_value ** 2, 4)

print(f"R-squared evaluation score is: {r2_score}")