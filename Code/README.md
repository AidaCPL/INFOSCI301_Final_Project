# CODE 

## **Overview**
This repository contains the research code for analyzing and visualizing misinformation dynamics across diverse datasets. The project integrates data from Climate-FEVER, FakeNewsNet, and a Global Misinformation Dataset to explore how misinformation spreads, clusters, and resonates within different social and cultural contexts. By leveraging advanced visualization techniques, machine learning, and Explainable AI (XAI), the research provides actionable insights for combating misinformation.

---

## **Key Features**

### **Datasets**
1. **Climate-FEVER**: A dataset with claims categorized as "supports," "refutes," or "not enough info," including corresponding evidence.
2. **FakeNewsNet**: Includes metadata for news articles, tweets, and user interactions, sourced from PolitiFact and GossipCop.
3. **Global Misinformation Dataset**: Behavioral and demographic data from 16 countries, focusing on variables like social media engagement and political alignment.

### **Functionality**
- **Data Preprocessing and Schema Alignment**:
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
  - `xgboost`

### **Installation**
Install the required Python libraries using the following command:
```bash
pip install pandas numpy matplotlib seaborn plotly shap xgboost
```

---

## **Usage**

### **Data Preprocessing**
1. Load datasets using the provided URLs.
2. Align and integrate the datasets:
   - Climate-FEVER schema is aligned with Global Misinformation data.
   - Combined dataset includes enriched metadata for behavioral analysis.

### **Machine Learning**
1. Train the XGBoost model on selected features (e.g., trust, political alignment, social media usage).
2. Evaluate feature importance using SHAP plots to understand the drivers of misinformation susceptibility.

### **Visualizations**
1. Generate SHAP summary and dependence plots to visualize model insights.
2. Create choropleth maps and network diagrams to explore misinformation patterns.
3. Use interactive dashboards for real-time filtering and analysis.

---

## **Files in the Repository**
- **`data_preprocessing.py`**: Scripts for loading and aligning datasets.
- **`model_training.py`**: Includes machine learning pipelines and SHAP analysis.
- **`visualization_tools.py`**: Functions for creating static and interactive visualizations.
- **`integrated_dataset.csv`**: Preprocessed dataset for analysis.

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