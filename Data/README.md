# DATA

This repository includes datasets for analyzing misinformation, focusing on environmental and general contexts. Below are the descriptions of the datasets, their origins, and how they contribute to the research.

## **1. [Climate-FEVER](climate-fever-dataset-r1.jsonl)**
### **Description**
- **Source**: Created by researchers from ETH Zurich, Google Research, and the University of Maryland.
- **Content**: A dataset of 1,535 real-world climate-related claims annotated with supporting, refuting, or insufficient evidence labels.
- **Features**:
  - Claims sourced from internet debates and fact-checking platforms like ClimateFeedback.org.
  - Evidence retrieved from Wikipedia and annotated to support or refute claims.
  - Annotations include the label categories: SUPPORTS, REFUTES, NOT_ENOUGH_INFO, and DISPUTED.
  
### **Relevance to Research**
- Focuses on climate misinformation, directly aligning with this project's goal of analyzing environmental misinformation.
- Provides structured claim-evidence pairs that can be used for claim validation and misinformation visualization.
  
### **How to Use**
- Use Climate-FEVER to validate claims about climate change and analyze how misinformation narratives are constructed.
- Incorporate its annotated claims into clustering and visualization tools to highlight trends and disputes in climate misinformation.
- The prepocessed Climate-Fever codes includes a csv version of the json file found online.


## **3. ["Understanding and Combating Misinformation Across 16 Countries" Dataset](Main.csv)**
### **Description**
- **Source**: Collected as part of a global study analyzing misinformation trends across 16 countries.
- **Content**:
  - Data from over 54,000 participants, including their perceptions of news articles and social media use.
  - Features include demographic data, social media habits, political alignment, and ratings of news credibility.
- **Variables**:
  - News types shared (political, science, celebrity, business, etc.).
  - Cognitive reflection scores, trust levels, and social media engagement metrics.

### **Relevance to Research**
- Provides cross-cultural insights into how misinformation spreads and is perceived globally.
- Offers demographic and behavioral data for understanding user credibility in different cultural contexts.
  
### **How to Use**
- Integrate with other datasets to analyze regional and cultural variations in misinformation patterns.
- Use participant ratings and engagement metrics to study the relationship between social media habits and misinformation susceptibility.


## **Integration Plan**
1. **Claim Validation**:
   - Use **Climate-FEVER** as the primary dataset for validating environmental misinformation claims.

2. **Social Context Analysis**:
   - Use engagement and behavioral metrics from the "Understanding and Combating Misinformation Across 16 Countries" dataset to enrich the analysis.

3. **Visualization**:
   - Combine claim-evidence pairs from Climate-FEVER with user behavior data to create visual dashboards highlighting cultural and contextual variations in misinformation.

4. **Cultural and Regional Analysis**:
   - Leverage demographic and engagement data from the global misinformation dataset to contextualize findings from Climate-FEVER.

---
By combining these datasets, this project will generate comprehensive insights into the spread and perception of misinformation, particularly in the environmental domain.

### **Dataset Roles in The Research**

### **Enhanced Dataset Description**

1. **Climate-FEVER**:
   - **Strengths**:
     - Focuses specifically on climate-related claims, with evidence annotations (SUPPORTS, REFUTES, NOT_ENOUGH_INFO).
     - Enriched with real-world claims, making it highly relevant for analyzing environmental misinformation narratives.
   - **Contribution**:
     - Enhances the credibility verification process by focusing on fact-checked environmental misinformation.
     - Serves as a benchmark for claim validation models.

2. **Global Misinformation Dataset**:
   - **Strengths**:
     - Provides a comprehensive cross-cultural dataset, enabling the exploration of how misinformation spreads in different regions and social contexts.
     - Offers granular insights into user behavior, political alignment, and platform engagement.
   - **Contribution**:
     - Enriches the analysis by introducing demographic, cultural, and behavioral dimensions.
     - Serves as a bridge between structured misinformation datasets (FakeNewsNet, Climate-FEVER) and real-world behavioral data.
   - **Potential Use**:
     - Investigate cultural influences on misinformation perception.
     - Explore correlations between user behavior and misinformation susceptibility.

---

### **Framework for Integrating the Two Datasets**

1. **Define the Objective:**  
   The primary goal of integrating the datasets is to create a unified dataset that combines demographic, behavioral, and contextual features (from one dataset) with claim or target labels (from the other). This integration enriches the feature set, enabling robust machine learning analysis.

2. **Identify a Common Key or Relationship:**  
   - **Direct Join:** If both datasets share a unique identifier (e.g., user ID or claim ID), a direct merge (e.g., using `pandas.merge`) is applied to align records.
   - **Approximate Match:** If no explicit key exists but a logical relationship (e.g., time or geographic location) can be inferred, features are aligned using these attributes.

3. **Feature Engineering:**  
   - Select relevant columns from each dataset, such as demographics (age, education) and behavioral data (social media usage) from the first dataset and target labels (e.g., misinformation susceptibility or claim categories) from the second.
   - Create derived features if necessary, such as grouping numeric variables into categories or encoding text-based data.

4. **Handle Missing Data:**  
   - Address null values by imputation (e.g., filling with means or medians) or exclusion of incomplete rows.
   - Ensure alignment between datasets by filtering rows present in both datasets post-merge.

5. **Normalize and Encode Features:**  
   - Standardize or normalize numeric data (e.g., scaling `age`) and encode categorical variables (e.g., one-hot encoding `urbanrural`) to prepare for machine learning.

6. **Split Data:**  
   - Separate the integrated dataset into training and testing subsets, ensuring balanced representation of the target variable across the split.

7. **Model Development and Validation:**  
   - Use the enriched dataset to train a machine learning model, such as Random Forest, leveraging the diverse features to uncover meaningful relationships.
   - Validate results using metrics (e.g., accuracy, precision, recall) to ensure the integration added value.

This framework ensures the combined dataset captures rich, multi-dimensional insights and enables accurate, actionable predictions.
