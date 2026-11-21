# insurance-fraud-detection
- This data project concerns an Exploratory Data Analysis and Machine Learning classification on an [Auto insurance fraud claims Kaggle dataset](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection/data), originally curated by Oracle for an [article](https://blogs.oracle.com/coretec/oracle-analytics-oracle-machine-learning-fraud-detection-using-unsupervised-and-supervised-machine-learning) as a demonstration for fraud detection with supervised and unsupervised machine learning. 
- The intention of the project mainly comes to understand the entire flow of fraud analytics, as well as ensuring a business-framed mentality of Data Science and its collaborative flow.
- Limitations come from missing metadata and unavailable supplementary documents: pricing or cost data, to then provide synthetic basis for financial analysis.

## Objectives
- The main objective of the project is to model a binary classifier for the auto insurance case, detailing potential financial impacts and claim characteristics on information gain; to serve operational and analytics processes.
- We then seek to answer the following business questions:
  1. How prevalent is fraud in the claims population, and its implications on the scale of the problem?
  2. Which claims characteristics show a statistically credible elevated fraud rate, versus those explainable by small-sample noise or statistical fluctuations?
  3. Can fraud be reliably predicted from claim/policy characteristics, and the tradeoffs of different modeling approaches?
  4. What is the estimated financial impact, based on synthetic assumptions due to missing information, of deploying the model(s), and how should flagged claims be handled operationally?
## Methods
1. [Exploratory Data Analysis](./notebooks/01_eda.ipynb)
   - Contains basic inspections of the dataset
   - Initially screened the data for minor data anomalies (Age=0 outliers, categorical label anomalies)
   - Data provides 15,420 claims with 14,497 legitimate and 923 fraud classifications, which defines the 5.99 % global fraud rate of the dataset
   - Purposefully implemented a hypothesis test on feature-category elevated fraud to flag higher than expected fraud that routes to either Exact Binomial or Poisson Approximation
   - Conducted tests and appropriately handled feature anomalies like the Age = 0 observations. Age provides the numeric 'continuous' data, where an existing AgeOfPolicyHolder contains bracketed age.
   - Further inspection between numeric Age and bracketed AgeOfPolicyHolder shows a data-quality issue where Age were not binned correctly on the brackets provided, which was then rebinned accordingly. 
   - This correction was done based on inferred evidence by numeric Age to AgeOfPolicyHolder bracket labels, given no official documentation existed. 
   - The Unknown ages were kept as their own bracket rather than imputed, to preserve any signal given by the missing values.
   - Applied Benjamini-Hochberg FDR correction, pooled across all 178 tested (feature, category) cells with a set q < 0.05 cutoff, reducing the flags from 29 to 20.
2. Feature Selection [Planned]
   - Association tests: Cramer's V (strength, bias-corrected) + Theil's U (directional dependence)
   - Redundancy among features: Variance Inflation Factor (VIF/GVIF)
   - To provide a summary of which features to keep, drop, or choose between.
3. Model Development [Planned]
   - Modeling a set of binary classifiers (fraud/legitimate) for insurance claims with Logistic Regression, Random Forest, XGBoost
   - To appropriately use data transformers that consider if the classifier is linear, tree-based, or boosting.
   - To then evaluate the models by appropriate metrics, Precision-Recall AUC (PR-AUC), especially for extreme class imbalance cases like fraud.
## Evaluation
Evaluating the results that come from performing the methods/processes
- To be completed after model evaluation
## Conclusion 
Derived metrics and significant measures/information from evaluation on the final output
- To be completed after model evaluation
## Recommendation
Key recommendations or explanations of what results from the analysis, what matters to the company, and its impact, as well as the next few steps to address fraud cases.
- To be completed after model evaluation