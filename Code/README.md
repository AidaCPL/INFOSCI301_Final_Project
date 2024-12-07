# CODE

## **Overview**

This repository contains the research code for analyzing and visualizing misinformation dynamics across diverse datasets. The project integrates data from Climate-FEVER and a Global Misinformation Dataset to explore how misinformation spreads, clusters, and resonates within different social and cultural contexts. By leveraging advanced visualization techniques and machine learning, the research provides actionable insights for combating misinformation.

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
  - **Interactive Visualizations**:
    - `/apps/intellect.py`: Code for the interactive visualization exploring the relationship between social media and critical thinking.
    - `/apps/network_app.py`: Code for creating interactive network diagrams to analyze misinformation pathways.

---

## **Getting Started**

### **Requirements**

- Python 3.8 or higher
- Required Libraries:
  ```
  pandas
  numpy
  matplotlib
  seaborn
  plotly
  shap
  ipywidgets
  sklearn
  dash
  networkx
  ```
- Install dependencies using the following command:
  ```bash
  pip install -r requirements.txt
  ```

---

## **Documentation**

### **How to Run the Code**

1. Clone the repository:
   ```bash
   git clone https://github.com/AidaCPL/INFOSCI301_Final_Project.git
   cd INFOSCI301_Final_Project
   ```
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the relevant scripts:
   - **Data Preprocessing**: Run `data_preprocessing.ipynb` to clean and align datasets.
   - **Machine Learning**: Use `machine_learning.ipynb` to train models and generate feature importance visualizations.
   - **Visualization Tools**:
     - Run `visualization_tools.py` for static plots.
     - Use `/apps/intellect.py` for exploring social media impacts interactively.
     - Use `/apps/network_app.py` for interactive network visualizations.
4. To explore the geospatial map:
   - Open the HTML file in the `/map` folder with any modern browser.

### **Environment Setup**

Create a virtual environment for the project:
```bash
python -m venv env
source env/bin/activate # On Windows use `env\Scripts\activate`
```
Install dependencies:
```bash
pip install -r requirements.txt
```

### **Example Usage**

#### Data Preprocessing:
```bash
jupyter notebook data_preprocessing.ipynb
```

#### Machine Learning Pipeline:
```bash
jupyter notebook machine_learning.ipynb
```

#### Interactive Visualizations:

1. Run the `intellect.py` script to explore relationships between social media and cognition:
   ```bash
   python apps/intellect.py
   ```
2. Run the `network_app.py` script to explore network diagrams interactively:
   ```bash
   python apps/network_app.py
   ```

---

## **Files in the Repository**

- **`data_preprocessing.ipynb`**: Scripts for loading and aligning datasets.
- **`visualization_tools.py`**: Functions for creating static and interactive visualizations.
- **`machine_learning.ipynb`**: Includes machine learning pipelines and SHAP analysis.
- **`/map`**: HTML file for the geospatial map that one can download and run on a browser.
- **`/apps/intellect.py`**: Interactive visualization for social media impact analysis.
- **`/apps/network_app.py`**: Interactive visualization for network analysis of misinformation.

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

For further questions or feedback, please contact any of the team members.
