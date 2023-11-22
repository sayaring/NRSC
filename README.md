# NRSC Screening


## Problem 1: Crop Recommendation System

This project comprises a Crop Recommendation System that assists in suggesting suitable crops based on various environmental factors. The system utilizes machine learning algorithms to predict the ideal crop for a given set of conditions, enabling farmers or stakeholders to make informed decisions regarding crop selection.

### Overview

The repository includes a Colab Notebook(Crop_Recommendation_System.ipynb) generated using Google Colab. The code leverages Python and several libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn to perform data analysis, model training, and evaluation.

### Data Exploration and Preprocessing

The initial phase involves exploring the dataset, which consists of information on environmental factors such as Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH, and rainfall. The data undergoes analysis, checking for null values, distribution, multicollinearity, and outlier presence. Visualizations such as bar plots and box plots help understand the relationship between different features and crop types.

### Model Training and evaluation

**Models Used:**
* Decision Tree: Utilizing DecisionTreeClassifier for classification tasks.
* Naive Bayes: Gaussian Naive Bayes model for classification.
* Random Forest: RandomForestClassifier to harness the power of ensemble learning.
* Gradient Boosting: GradientBoostingClassifier for boosting model performance.

**Model Comparison:**
The notebook compares the performance of these models by evaluating accuracy scores and training times. Each model undergoes training using the dataset and is evaluated against test data, providing insights into their respective accuracies and computational requirements.

### Conclusion
Based on the comparison results, the Gradient Boosting algorithm demonstrates the highest accuracy, albeit with a relatively longer training time. However, considering the trade-off between accuracy and training time, Naive Bayes or Random Forest could serve as suitable models for this particular application.

## Problem 2: Deforestation Forecast Analysis

The Deforestation Forecast Analysis project focuses on analyzing and visualizing the trend of deforestation in specific regions, aiming to understand and highlight areas requiring conservation efforts. Utilizing data analysis and visualization techniques, this analysis provides insights into deforestation trends over a 15-year period.

### Overview
The analysis is performed using Jupyter Notebook (Deforestation_Analysis.ipynb) within Google Colab. Python is the primary programming language, and libraries such as Pandas, NumPy, Matplotlib, Plotly, and Re are employed to conduct data preprocessing, exploratory analysis, and visualization.

### Exploratory Data Analysis

The analysis commences with data exploration and preprocessing. The dataset (def_area_2004_2019.csv) contains information on deforested areas across different states over a period of 15 years. The initial steps involve examining data structure, descriptive statistics, and renaming fields for better understanding.

### Analysis and Visualization

**Total Deforested Area per Year:**
Visualizations, including bar plots and trend lines, showcase the total deforested area per year, highlighting trends and fluctuations over the analyzed period.

**Deforestation by State:**
Analysis based on individual states reveals the cumulative deforested areas, identifying states with above-average deforestation rates and presenting trends over time for each state.

**Deforestation Trend Analysis:**
Detailed trend analyses for high-deforestation states like Mato Grosso, Para, and Rondonia are depicted through line charts, providing insights into the periodic spikes in deforestation.

**Heatmap Visualization:**
A heatmap visualization offers a comprehensive overview of deforestation trends across states over the analyzed years, reinforcing earlier analyses and emphasizing critical time points.

### Conclusion
The analysis concludes by identifying regions requiring urgent conservation efforts, namely Para, Mato Grosso, and Rondonia. It emphasizes the significance of addressing deforestation in these areas to prevent further environmental degradation.

