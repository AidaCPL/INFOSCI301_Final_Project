# DATA

This repository includes datasets for analyzing misinformation, focusing on environmental and general contexts. Below are the descriptions of the datasets, their origins, and how they contribute to the research.

## **1. [FakeNewsNet](politifact_fake.csv)**
### **Description**
- **Source**: FakeNewsNet is a comprehensive dataset curated by researchers at Arizona State University and Penn State University.
- **Content**: It includes news articles and related social media data focusing on misinformation in two domains:
  - **PolitiFact**: Contains fact-checked political news (real and fake).
- **Features**:
  - **News Content**: Text of fake and real news.
  - **Social Context**: User interactions such as retweets, likes, and comments (not included in the minimal dataset due to privacy policies).
  - **Spatiotemporal Information**: Temporal and geographic patterns in news dissemination.
  
### **Relevance to Research**
- Helps analyze how misinformation spreads across different social contexts and domains.
- Offers insights into political and entertainment misinformation, which can be compared with environmental misinformation patterns.

### **How to Use**
- Use the **PolitiFact** subset for analyzing news content and fake news patterns related to governance and policy, including climate policy misinformation.
- Compare the propagation dynamics from the social context (when available) with patterns in environmental misinformation datasets.


## **2. [Climate-FEVER](/Users/aidacamacho/Desktop/github/INFOSCI301_Final_Project/Data/climate-fever-dataset-r1.jsonl)**
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


## **3. ["Understanding and Combating Misinformation Across 16 Countries" Dataset](/Users/aidacamacho/Desktop/github/INFOSCI301_Final_Project/Data/Main.csv)**
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
   - Compare its annotations with **FakeNewsNet's** PolitiFact subset to analyze overlapping patterns in fake news narratives.

2. **Social Context Analysis**:
   - Integrate **FakeNewsNet's** social context features (if available) to study user interactions with misinformation.
   - Use engagement and behavioral metrics from the "Understanding and Combating Misinformation Across 16 Countries" dataset to enrich the analysis.

3. **Visualization**:
   - Combine claim-evidence pairs from Climate-FEVER with user behavior data to create visual dashboards highlighting cultural and contextual variations in misinformation.

4. **Cultural and Regional Analysis**:
   - Leverage demographic and engagement data from the global misinformation dataset to contextualize findings from Climate-FEVER and FakeNewsNet.

---

By combining these datasets, this project will generate comprehensive insights into the spread and perception of misinformation, particularly in the environmental domain.

### **Dataset Roles in The Research**

### **Enhanced Dataset Description**

1. **FakeNewsNet**:
   - **Strengths**:
     - Offers a multi-domain perspective with political and entertainment news, annotated for misinformation.
     - Includes social context (engagement data such as retweets, replies, and likes) and metadata (user profiles, timestamps, etc.).
   - **Contribution**:
     - Provides insights into user engagement and the mechanisms of misinformation spread on social media, which can be adapted to study environmental misinformation.
     - Helps model the social dynamics that drive the dissemination of misinformation across topics.

2. **Climate-FEVER**:
   - **Strengths**:
     - Focuses specifically on climate-related claims, with evidence annotations (SUPPORTS, REFUTES, NOT_ENOUGH_INFO).
     - Enriched with real-world claims, making it highly relevant for analyzing environmental misinformation narratives.
   - **Contribution**:
     - Enhances the credibility verification process by focusing on fact-checked environmental misinformation.
     - Serves as a benchmark for claim validation models.

3. **Global Misinformation Dataset**:
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

### **How to Combine These Datasets**

1. **Mapping Across Datasets**:
   - Use **Climate-FEVER** to validate claims related to climate misinformation.
   - Incorporate **FakeNewsNet**'s metadata and context for analyzing dissemination patterns.
   - Leverage the **Global Misinformation Dataset** to explore behavioral and cultural dimensions.

2. **Framework for Integration**:
   - **Schema Alignment**:
     - Standardize variables across datasets (e.g., claim validation, user engagement metrics).
   - **Data Fusion**:
     - Augment climate-related claims in Climate-FEVER with user behavior from the uploaded dataset.
   - **Visualization**:
     - Create dashboards mapping misinformation themes across cultural and behavioral dimensions.

3. **Clustering and Insights**:
   - Use clustering to identify overlapping misinformation themes (e.g., climate, politics).
   - Analyze how misinformation resonates differently across cultures and social media platforms.

---

### **Potential Benefits of Combining These Datasets**
- **Cross-Domain Analysis**:
  - Investigate whether patterns of misinformation dissemination in politics differ from environmental contexts.
- **Behavioral Insights**:
  - Explore how social media behavior affects the spread of misinformation in different regions.
- **Enhanced Visualizations**:
  - Use rich metadata to generate interactive tools for analyzing user engagement and misinformation trends.
