# Progress Log

## 07-16-26
- Initiated data project
- Created project structure and initial set of dependencies
- Done: Drafted the initial set of repositories/folders/ignored files
- To do: data sourcing, eda, and set up environment

## 07-22-26
- refactored python virtual environment for the project
- reinstalled dependencies
- separated folders for the dependencies of the project for runtime/dev
- Done: set-up environment and dependencies
- To do: data sourcing, eda, analysis

## 07-29-26
- sourced dataset from kaggle
- loaded and inspected proper reading of the dataset
- drafted domain_notes of the project
- fixed unstaged changes from a supposed previous commit in setup-requirements branch
- Done: sourcing, initial outline/draft of context, fixed uncommited/unstaged changes
- To do: eda, initial analysis, context build-up

## 07-30-26
- initial draft of domain notes
- identified core sources for note-taking
- to do: eda, initial analysis, context build-up

## 08-31-26
- project resumed (pause due to device repairs)
- finished first set of domain notes
- done: context build-up
- to do: eda, analysis

## 09-15-26
- continued eda
- created an eda_utils module for eda-specific functions
- to do: migrate functions defined in the eda notebook to the module

## 09-26-26
- eda continuation
- to do: create modeling and business intelligence tables

## 10-06-26
- eda continuation
- finished distribution checks and testing descriptions
- to do: refactor eda_utils plotting functions, create modeling and bi tables

## 10-08-26
- eda continuation
- distribution analysis and anomaly/outlier treatment
- to do: define association functions and description, create eda summary

## 10-15-26
- eda continuation
- added hypothesis section for reference in eda
- initial analysis on distribution checks
- significance tests to be pooled for correction against multiplicity
- to do: revise hypothesis-test function, formalize association functions and descriptions, draft eda summary

## 10-19-26
- eda continuation
- started revising the plotting/test function; an OOP registry involved
- decided to stipulate an additional factor, multivariate analysis
- to do: finish the registry function and plotting function, formalize association tests and descriptions, draft multivariate analysis

## 10-21-26
- eda continuation
- fixed plot_discrete_class plot function and renamed as explore_discrete_feature
- formalized the EDAFraudRegistry as an OOP instance for handling the global FDR correction
- to do: bivariate analysis, multivariate analysis, eda summary, table creations

## 10-24-26
- eda continuation
- bivariate (distribution by target) analysis
- to do: eda summary

## 10-28-26
- eda continuation
-  bivariate (distirbution by target) analysis
- outlier/anomaly detection
- encountered anomaly in age/bracketed_age; to relabel/bin appropriately
- to do: treat anomalies, finish bivariate (distribution by target) analysis, start context for bivariate (associations) and mutivariate analysis

## 10-31-26
- eda continuation
- diagnosis attempt on age/bracketed_age anomalies
- to do: treat anomalies, finish bivaraite (distribution by target) analysis, start context for bivariate (associations) and mutivariate analysis

## 11-13-26
- eda continuation
- documented age anomaly and conducted appropriate statistical tests
- to do: document bivariate (distribution by target) analysis summary, context for bivariate (associations) and multivariate analysis, table creations, formalize feature selection

## 11-14-26
- eda continuation
- correctly-binned age to appropriate brackets
- performed the FDR-BH correction for the categorical features
- to do: document bivariate (distirbution by target) analysis summary, context for bivariate (associations) and multivariate analysis, table creations, formalize feature selection

## 11-16-26
- eda continuation
- finished per-feature distribution check analysis
- to do: context for bivariate (associations) and multivariate analysis, table creations, formalize feature selection

## 11-21-26
- eda continuation
- documented findings from FDR-BH corrected tests
- reworked README.md
- to do: bivariate, multivariate context, creating new branch for feature-association-selection

