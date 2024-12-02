# CODE 

## **Overview**
This repository contains the research code for analyzing and visualizing misinformation dynamics across diverse datasets. The project integrates data from Climate-FEVER and a Global Misinformation Dataset to explore how misinformation spreads, clusters, and resonates within different social and cultural contexts. By leveraging advanced visualization techniques,and machine learning, the research provides actionable insights for combating misinformation.

---

## **Key Features**

### **Datasets**
1. **Global Misinformation Dataset**: Behavioral and demographic data from 16 countries, focusing on variables like social media engagement and political alignment.
2. **Climate-FEVER**: A dataset with claims categorized as "supports," "refutes," or "not enough info," including corresponding evidence.

### **Functionality**
- **Data Preprocessing**:
  - Standardizes schemas across datasets to enable seamless integration.
  - Saves aligned datasets for further analysis.
- **Integrated Dataset Creation**:
  - Combines datasets to enrich analysis with cross-referenced information.
  - Adds demographic and behavioral metadata for deeper insights.
- **Machine Learning and Explainable AI**:
  - Trains an XGBoost model to predict misinformation susceptibility based on user behavior and contextual variables.
  - Uses SHAP (SHapley Additive exPlanations) to analyze feature importance and interactions.
- **Visualization Techniques**:
  - Choropleth maps for regional analysis of misinformation.
  - Network diagrams for visualizing connections between misinformation clusters.
  - SHAP dependence plots and summary plots to interpret model predictions.

---

## **Getting Started**

### **Requirements**
- Python 3.8 or higher
- Libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `plotly`
  - `shap`
  - `ipywidgets`
  - `sklearn`

### **Installation**
Install the required Python libraries using the following command:
```bash
pip install pandas numpy matplotlib seaborn plotly shap ipywidgets sklearn
```

---

## **Usage**

### **Data Preprocessing**
1. Load datasets using the URLs under the data folder on this repository.
2. Clean and preprocess data

### **Machine Learning**
1. Train the Random Forest model on selected features (e.g., contextual information, social media usage).
2. Evaluate feature importance using bar and SHAP plots to understand the drivers of misinformation susceptibility.

### **Visualizations**
1. Generate SHAP summary and dependence plots to visualize model insights.
2. Create bar plots to visualize feature importance.

---

## **Files in the Repository**
- **`data_preprocessing.ipynb`**: Scripts for loading and aligning datasets.
- **`visualization_tools.py`**: Functions for creating static and interactive visualizations.
- **`machine_learning.ipynb`**: Includes machine learning pipelines and SHAP analysis.
- **`/map`**: HTML file for the geospatial map that one can download and run on browser.
---

## **Results**
The research highlights:
- Regional patterns in misinformation detection capabilities.
- The influence of cultural and social factors on misinformation spread.
- Insights into misinformation clusters and amplification dynamics.

---

## **Contributions**
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

--- 

## **Contact**
For further questions or feedback, please contact any of the team memebers. 