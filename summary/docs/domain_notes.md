# Automotive Insurance Fraud
This end-to-end data project deals with the use of a class-imbalanced dataset sourced from kaggle to detect fraud and imply on its implications to an enterprise by means of general insights, model development, and impact assessment.

## Project Objectives
This analysis on the Auto-Insurance dataset aims to detect fraud instances, where then we derive quantitative metrics that measure the impact of fraud to an insurance enterprise. Through this project, the analysis aims to answer the questions:
1. What is the total number of fraud and legitimate transactions?
2. How much is lost due to fraud?
3. What characterized descriptions (features) show the highest instance of fraud?


## The Automotive Industry
In general, the industry deals with manufacturing motor vehicles, by which, most primarily deal with passenger automobiles; secondary to this are commercial vehicles, which themselves, are important to the industry as a whole.
- Although the industry focuses on manufacturing in the literal sense, an enterprise-scale entity involves itself in subsequent activities that follow the creation and sale of these products.
- The automotive industry only handles the part of product creation, which dealers then sell, and insurers finance its longevity of use
- Car insurance or autoinsurance is a matter dealt with by insurance companies, which are third-party to the primary manufacturers of cars; this pertains to a direct extension of sale to that of financial and property security.

## Insurance
An industry that operates by covering extreme losses at a particular profiled cost
- Estimates an event-particular loss distribution, taking advantage of the unlikeliness or outlying accidents in a certain industry 
- It finances itself from a large number of contributors to redistribute to a select few cases of incidences.
- Through its allocations and plan profiles, the industry conforms to more of a "trust-based" entity, where contributors at a "premium" are paying for a future unlikely occurence; essentially defined as a personl security investment.
### Insurance Claim Lifecycle
When an accident or particular event covered by a contributor's premium insurance plan happens, individuals are subject to a structured flow to file an insurance claim:
1. First Notice of Loss (FNOL)
   - Customer informs the company about the occurence of a "covered event"
   - Covered events are those explicitly mentioned in a customer's premium or policy plan, by which they can claim for insurance
   - The FNOL report involves documentation regarding the incident: involvements, description, time, place, evidences, and supplemental reports
2. Triage & Assignment
   - When a claim is filed, the company categorizes based on complexity, severity, and coverage type
   - Simple claims may be somewhat automated; whereas those with significant financial coverage or complex cases are handled by an assigned company specialist
3. Coverage Verification & Reserving
   - With the incident reported and assigned to specific handling departments, the insurer reviews the file by inspecting and verifying coverage through policy or premium paid for by the customer.
   - By this stage, the insurer can assess the type of loss, exclusions, deductibles, and policy limitations to mitigate and allot reserved financing of each claim
4. Investigation & Assessment
   - The stage where detailed assessment and fact-finding occurs; often requiring a longer duration in the claims lifecycle
   Involves investiagtion at the loss site, estiamtion from contractors or facilities, records, witness statements, interviews, experts, and third-party data sources which may provide better context for the validity and severity of the claim.
   - At this stage, the claim may be apprehended for **potential fraud**, a case that becomes crucial to the entire distribution mechanism of financing insured losses.
   - Insurance companies often utilize a claims management system for field adjusters to upload documents or supporting evidences that would aid with defending or reassessing a claim.
5. Evaluation (Liability & Damages)
   - With the damages and policy coverage verified, the clims can then move to an evaluation stage.
   - At this point, it comes to ask **who is responsible**, that could very well "tip the scales" in liabilities.
   - Along with determining the cause, comes calculating the **Actual Cash Value (ACV)** vs **Replacement Cost Value (RCV)**
   - **ACV** refers to a depreciated value for the damaged property from its age and condition
   - **RCV** refers to the cost of replacement with new materials of the same kind and quality.
   - It comes by a matter of policy outlining to whom the ACV or RCV could be applied.
6. Settlement Decision
   - The stage that sums up the investigated and evaluated claim for a decision for the case
   - The claim may be approved in full, in part, or denied, by where exclusions or policy terms may twist the verdict that comes out.
7. Payment & Repairs/Benefits
   - Approved claims follow local payment laws which may be a direct bank deposit, physical check, direct repair facility or contractor, or toward certain providers.
   - Local state laws, that is if the insurer follows a federal system of some kind, often have a set maximum payment window after a certain number of days since the agreement.
### Autoinsurance
The automotive industry branches to an external entity for insurance enterprises, by which comes the offer for autoinsurance
- In this context, autoinsurance pertains to a contract or policy between an insurer and a driver.
- Insurance in this case protects the contributor (driver) in cases of extreme losses against theft, accidents, or damage.
- An insurance company collects premium, a periodic payment from drivers/contributors, as a source for financing the loss.
- Although premium plans and coverages may vary, states or governing bodies may impose a minimum liability coverage on insurers, allowing a floor-price for eligible claims.
### Autoinsurance and its Coverage
As with policies and plans, in general, autoinsurance covers financial losses that stem from vehicular damage, property damage, bodily injuries, medical/funeral bills.
- The design towards these premium plans depend on the insurer's evaluation of factors, including but not limited to:
  - gender
  - age
  - years of driving experience
  - accident and relevant violation history
  - among other contributing factors;
- Based upon the standard lifecycle of an insurance claim, cases in the Philippines go through a similar filing flow. 
- Basic requirements remain as follows:
  - Copy of Policy/Premium document with receipt of latest payment
  - Police Report Affidavit
  - Photographs
  - Notarized Affidavid or Insurance Claim Form from Insurer
- From ichoose.ph, the process may differ by the nature of the case
  - **Own Damage/Theft of Parts**
    - In cases where the contributor caused damage to their own property.
    - Varies by premium coverage as to what degree of personal causality may be covered
    - It is best to prepare the standard requirements,to then wait for inspection and assessment
    - By a matter of how your insurer works, provided financing may be after-the-fact of repairs or parts replacement, when claim is indeed valid
  - **Personal/Passenger Injury or Death/Accident**
    - On top of the basic requirements, copies of medical documents (receipts and prescriptions), death/funeral certificates, or even certificate of employment may be asked
  - **Lost or Stolen Vehicle**
    - With insurance companies composed of varying divisions for different cases of claims, comes proper submission to the appropriate group, i.e. Anti-Car napping Group
    - May require documents stemming from original complaint, LTO or Registration papers, ignition keys, i.e. documents that would support ownership and supplemental for criminal evidence
  - **Natural Disasters**
    - Insurers may offer an **Acts of Nature** coverage, which is a longer insurance claim case.
    - Despite being longer in nature, it is often easily verifiable,as more than often, it comes from a mass-property loss, i.e. flood.
- As mentioned, state laws may provide a time duration for repayment or insurance financing, by which the Philippines follow a 3-month waiting period for car recovery, where the ACV is then paid as an alternative after the window.
## Insurance Fraud
The intentional act of providing false or manipulated documents and personal accounts when filing an insurance claim.
-  The aim of insurance fraud usually pertains to an unfair financial gain, which would've been, otherwise properly allocated to truthful and necessary claim cases.
- Additional to document falsification, insurance fraud may happen in the case of: staged accidents, third-party theft, as well as in-house attempts of fraud from the insuring company.
- It is common to question **why fraud matters**, as it does stem from a thinking that these corporate entities may be taking advantage of its contributors. Yet more than often, the necessity of insurance enterprises arise with the fact that people require financial security at the event of extreme losses.
- To answer the question on why one should care about fraud, it pertains to general aim of properly financing the actual needs of its beneficiaries. With insurance fraud, not only does the business lose profit; it stops the ability of financing loss from outlying fraudulent claims.
### Auto Insurance Fraud
Fraud in auto insurance pertains to deliberate tactics, i.e. report manipulation and liability implications, that hinders a company to finance replacements, or thereof covering the costs of bodily treatments of drives (policyholders).
- Insurance fraud in the automotive industry happens through a number of ways:
  1. Report of Loss: document falsification
     - The most common facet of insurance fraud where injuries, car damage, and fake incidents are reported to the insurer. A false report, given notice in the **investigation and assessment** stage of the claims lifecycle circles back to the **first notice of loss** filed by the contributor.
     - By this, investigation and counter-evaluations are essential to proper allotment of insurance claims
  2. Auto Repairs: counterfeits and misquotes
     - Happens with the involvement of third-party or untrustworthy mechanics and body shops. 
     - These entities may commit fraud by replacing car parts with fake and fragile components, or by giving higher-than-standard estimates for repairs.
     - These types of fraud not only increase the price of premium paid by the customer, but also harm the driver/policyholder in accidents where safety features may have otherwise prevented injury
  3. Staged Crashes: third-party organized crime
     - An instance of fraud where a third entity, another driver, fakes an accident by directly causing it.
     - When this happens, medical and car repair bills may be insured, that it turn would increase your paid policy plan along with other customers
     - The FNOL should be given high importance with respect to what evidences have been collection, i.e. the existence of dashcams and personal recordings.
### Classifying Fraud
Auto insurance fraud, like fraud in other industries, can be classified by how it occurs. This distinction creates a division for appropriate detection metrics and analysis to be chosen, as well as the entire machine learning methodology used for the analysis.
- **Hard Fraud**
  - A type of insurance fraud where **no real damage exists with an entirely false claim**
  - Alternatively, the damage may have been self-inflicted
  - By this classification, investigation and assessment measures require deep inspection that would indicate non-incidental damages, or at a much broader and concurrent case of organized crime.
- **Soft Fraud**
  - An insurance fraud that exaggerates an incident or insurance-covered loss, i.e. a bumper dent that's been modified in the FNOL as the loss of the specific car part.
  - These can stretch to creating additional claims that, initially only pertains to hit-and-run accidents, to a medical claim for injury.
- With the reach and societal contribution of the insurance industry, any indication of fraud from an insurance claim necessitates a heavier push for investigating and assessing an FNOL, those involved, additional evidences that may have been missed, and a consultation with field experts.
### Detection and Caveats
From the insurance claim lifecycle, fraud can be determined through investigation and assessment activities. 
- An insurance enterprise would have to go through each report manually to spot inconsistencies by inspection. However, insurance, by an estimate, is a multi-billion dollar industry, where reports would surmount to a number that manual investigation cannot handle. 
- Along with this, the fact that it is an assessment for possible fraud indicate an uncertainty of flagging them as such, i.e. resulting in capital loss or slow financing when missing fraudulent claims, as well as ensuring seamless insurance transactions, respectively.
- It is then important to discuss the progression of processing claims, flagging fraud, inspecting, and evaluating with the business context for the industry.
#### Handling Class Imbalance
There are data pre-processing steps required to make a dataset appropriately formulated for methodologies. One of these steps in the frame of fraud detection is handling **class imbalance**, this is because fraud is scarce in a dataset filled with legitimate transactions. Primarily, the reason why we account for class imbalance is the fact that it directly affects how methods or machine learning models predict the class of a transaction. While many class imbalance strategies are available, some are noteably used especially for fraud detection.
1. Random Over/Undersampling: Undersampling and Oversampling are two separate strategies that are sometimes combined. Undersampling refers to taking fewer samples from the majority class, helping to reduce imbalance. Oversampling on the other hand, is done for the minority class where new samples are created by synthesizing/duplicating them. When combined, along with a subvariant for randomness, or random under/oversampling, the strategy balances the distribution of data that there are equal counts for both classes. It may help with addressing model's poor performance in prediciting the minority class, but as much as with creating duplicated or synthetic observations, this method is subject to overfitting the minority.
2. SMOTE: A method that selects samples that are close in the feature space. A random sample from the minority class is first chosen, where then the k-nearest-neighbors to the sample, usually k=5 are found. With this, a synthetic sample is created at a random selected point on the line between chosesn samples of each of the nearest neighbors to the original sample. This strategy is often effective since new synthetic samples from the minority are actually created considering feature relationships as observed in a feature space. SMOTE consists of variations, i.e. SMOTE-TOMEK that interpolates neighbor samples rather than direct duplication, SMOTENC which is an extension of SMOTE that notices numerical and categorical features,
3. ADASYN: A strategy similar to SMOTE that adds a random small value to points after creating the synthetic samples, since it would introduce a bit of variance than a direct linear correlation to the parent sample.
- There are other class imbalance strategies that could be considered, i.e. **this section may then expand further when EDA and dataset inspection transpires for better pre-processing treatment**
#### Traditional detectors
Insurance companies have pre
dominantly gone through reports by manual means, having a great number of manpower to decode and decide upon insurance claims.
- In the automotive insurance industry, this would mean having to review accident footage, go through medical histories and records, as well as finding specific clauses in a policyholder's covered set of claims in their premium.
- Although these manual steps may have been sufficient, or still viable for small-scale insurers, the process requires aspects of semi-automations to handle a greater number of insurance claims.
#### Modern Detectors
Insurers, at present, use a variety of methods that is specific to their respective fields; filtering to classify claims as fraud or not. Majority, if not all fo these methods make use of AI or some form of automation in handling claims. To some extent, it is however important that human intervention is still considered a major factor in judgement on detected possible fraud. A literature review by [Schrijver et. al (2024)](https://www.sciencedirect.com/science/article/pii/S2667305324000164#kws0010) found a variety of current detection workflows for autoinsurance in recent studies.
- Fraud is something that occurs as an anomaly or outlier, which is why it is important to establish that fraud datasets are often, if not all the time, imbalanced; where fraud data is only a tiny fraction of the entire dataset that then indicate careful treatment and evaluation.
- In essence, a fraud detection workflow goes through a set of stages:
  1. Sampling: pertaining to strategies of data use and treatment
  2. Detection: training, calibrating, and testing a machine learning model
  3. Evaluation: determining the precision and recall of detections made
- Detections are mostly predicted with a supervised learning approach; where a dataset pre-labeled or known fraud and non-fraud cases are used to train a model, that is then used to test on new and unseen data.
  - Which can be by:
    - Rule
    - Neural Network
    - Ensemble Learning
    - Graph
    - Natural Language Processing
- From the literature review, five supervised techniques are commonly used; in decreasing order of frequency:
  - Random Forest: An ensemble learning approach that uses a bagged ensemble of decision trees, extending it to providing each learning tree with a random sample of training data, along with a random selection of all available features.
  - Logistic Regression: A standard base classifier that is most often used as a "baseline" for model comparison. Despite its simplicity, logistic regressions usually still perform well on various cases.
  - Support Vector Machine: A linear classifier that makes use of a hinge loss with an L2 regularization to maximize formed boundaries of classes, i.e. formation of margins. This classifier performs well for continuous variables, taking advantage of feature values themselves, therefore it is not beneficial to make use of them for majorly categorical features.
  - Decision Tree: A classification method that uses a tree, learning a sequence of if-else questions for the features of a dataset to predict class
  - Extreme Gradient Boost: An ensemble learning that involves training and combining weak classifiers that trains sequentially where each base/weak learner corrects the errors of the previous one. XGBoost shows effectiveness in classifying claims to the right categories.
- Although the literature review mentions the use of unsupervised learning, i.e. graph-based and other relevant techniques, applications of these workflows tend to be used for high-cost or non-available ground truth labels for model comparison. Extending this, graph-based methods require extensive use of relational fields, which is mostly unavailable for single-sourced datasets; this necessitates external or appended datasets that can be difficult to source out of an organization/enterprise. It may be worth exploring when taking on projects that mention anomaly detection, not something applicable to the project at hand.
- Note: With the numerous methods used for automobile fraud detection, this project will make use of Logistic Regression (baseline), Random Forest, and XGBoost for the predictions. README will stipulate why these models will be used for this specific analysis.
### Tradeoffs and Evaluators
Classification machine learning models can be evaluated through how well they predict/determine the class of a sample. With many evaluation metrics available, each has its own case usage that depends on the project objective and is tailored to the field or business context and what should be "saved" or "caught" by the model. 
#### Model Performance Metrics (Hard Predictions)
- Models can be evaluated as how well it predicts the classes, directly measuring the number, proportion, or mean of true and falsely-classified observations.
1. Accuracy: tells how many observations are correctly classified among the total records. Although it is used quite often, since fraud data is imbalanced where most is non-fraud and a minority of fraud instances, a prediction that always outputs a non-fraud prediction would score high accuracy despite not getting a single fraud prediction right. 
2. Precision: Measures how confident the model is that the predicted classifaction is actually true. It looks at the ratio of true positives over the sum of true and false positives. For fraud, it evaluations how confident the model is that the detection is a real fraud case.
3. Recall: Measures how confident the system is in catching all the fraud cases. It compares the ratio of true fraud to the sum of true and falsely-detected fraud cases.
4. F1-score: A single metric combining a model's precision and recall evaluations. It is especially used on imbalanced datasets. F1 score combines the two metricss through the harmonic mean rather than standard average, penalizing extreme differences between the two metrics. Aiming for a high F1 score means needing both a high precision and recall metric.
#### Model Performance Metrics (Probabilities)
- In the model-building or selection phase of a data project, it is often necessary to evaluate probabilities of model predictions, rather than hard/binary classes. In this case, when comparing models, you observe which of them understands or performs better on the dataset.
1. ROC-AUC: The area under the curve that plots the true positive rates against false postiive rates across all thresholds. It measures the probability that a random positive prediction will be ranked higher than a randomly chosen negative prediction. It performs well on balanced datasets, yet it becomes highly misleading for imbalanced or fraud datasets as it would highlight positive predictions more in the presence of a majority class.
2. PR-AUC: The area under the curve plotting Precision against Recall across all probability thresholds. It is ideally used in heavily-imbalanced binary classification with a focus on the minority or singificanlty-lower-count class. It is a recommended metric for fraud detection at it focuses excluseively on fraud, ignoring legitimate transactions. In the event that a model flags a lot more legitimate transactions just to catch a few fraud cases, the precision plummets, reflecting directly on the PR-AUC metric.
3. Log Loss: A metric that measures the distance between the predicted probabilties of observations and the actual binary class outcome. It penalizes the model for being too confident on wrong classifications. It is ideal for optimizing and training classifiers where the exact probability matters. It can be useful for training but it is most certainly bad for business logic as it evaluates on all observations/cases equally that would then ignore a number of fraud cases.
#### Detection Tradeoffs
In fraud detction the evaluation metrics used come as a tradeoff between Precision-Recall. When targeting to increase precision, we may detect less fraud and thus decreate Recall. Preferring recall on the other hand, detects more fraud but legitimate observations may be misclassified as such. It is entirely upon the focus of a business to which extent of trade-off would be preferred, highlighting either the need for reducing false detections or aiming to detect all instances of possible fraud.
#### Flagging vs Automation
As popularly stated, all models are wrong but some are useful. With this comes the necessary intervention of human capacity. Although some tasks may be automated, i.e. inputs, core logic, and structuring workflows; instances that require decision-making should have human intervention. This discussion highlights the fact that when we create these machine learning models, we merely "flag" observations of interest, rather than automate decisions if these cases are actual fraud.
### Fraud Detection in a Business Lens
Model building requires a certain level of nuance of business context. It matter most when determining what should be flagged or considered in building a detection system. In detecting fraud, although models are used to find patterns in the dataset and flagging them as fraud or legitimate, it may not direct sense or be interpretable in a business lens. It then becomes necessary to frame models that they become interpretable, by means of model explainability, to allow further discussion to take place, as it is at most, a business decision. Further into this, an analyzed dataset is only good with its relative context, as such, business pricing, loss, and profit become core to data project reports. All this entirely frames the structure of model development in the viewpoint of a business venture.
#### Insurance Premiums and Detection Crossing 
## The Project Data

### Data Dictionary

### Discussion Thread Points
- From kaggle, giving information of how much analyses have been done previously on the dataset, what has been used, and of course its contents and some additional information
### Synthesizing Missing Information

## References
- [Defining the Automotive industry](https://www.britannica.com/technology/automotive-industry)
- [Defining the Insurance industry](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/373041468330330962)
- [Cycle of an Insurance claim](https://vcasoftware.com/life-cycle-of-an-insurance-claim/)
- [Auto Insurance](https://www.investopedia.com/terms/a/auto-insurance.asp)
- [Fraud by the Coalition Against Insurance Fraud](https://insurancefraud.org/fraud-why-care/)
- [Auto Insurance Fraud](https://insurancefraud.org/scam-alerts/)
- [Hard and Soft Fraud](https://www.drodermiller.com/blog/2021/06/hard-and-soft-insurance-fraud-whats-the-difference/)
- [Literature Review Research on Autoinsurance fraud detection](https://www.sciencedirect.com/science/article/pii/S2667305324000164)
- [Class Imbalance in Fraud Detection](https://medium.com/data-reply-it-datatech/imbalanced-classification-in-fraud-detection-8f63474ff8c7)
- [Vehicle Insurance Claim Fraud Detection - Auto Insurance Dataset](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection/data)


