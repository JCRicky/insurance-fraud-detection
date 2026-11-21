"""Module for eda functions and type-specific visualizations."""
#packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import seaborn as sns
import scipy.stats as stats
from statsmodels.stats.multitest import multipletests

# metadata and statistical metrics summary function
def eda_summary(df):
    """Generates a DataFrame that summarizes basic inspection for Exploratory Data Analysis (EDA)."""
    # 1. Basic Metadata (current dtype, null/non-null,unique counts)
    summary = pd.DataFrame(
        {
            "dtype": df.dtypes,
            "non_null_count": df.notnull().sum(),
            "missing_count": df.isnull().sum(),
            "n_unique": df.nunique()
        }
    )
    # 2. Summary statistics
    desc = df.describe(include='all').T #transposed describe output

    # 3. Combining metadata and stats
    stat_cols = ['mean','std','min','25%','50%','75%','max']
    summary = summary.join(desc[stat_cols], how='left')
    summary['mode'] = df.mode().dropna(how='all').iloc[0]
    summary["skewness"] = df.skew(numeric_only=True)
    summary["kurtosis"] = df.kurtosis(numeric_only=True)
    summary = summary.sort_values(by="dtype", key=lambda x: x.astype(str), ascending=True)
    return summary

class FraudEDARegistry:
    def __init__(self):
        # storing hypothesis test metadata and results
        self._test_records = {}

    def test_log(self, feature_name, category, fraud_count, cell_total, expected_fraud, local_fraud_rate, global_baseline, test_used, p_value):
        """Logs cell tests in features to return p-value significance indicator."""
        # Create the unique composite key
        test_key = (feature_name, category)
    
        if test_key not in self._test_records:
            self._test_records[test_key] = {
                'Feature': feature_name,
                'Category': category,
                'Fraud_Count': fraud_count,
                'Category_Total': cell_total,
                'Expected_Fraud': expected_fraud,
                'Local_Fraud_Rate': local_fraud_rate,
                'Baseline_Rate': global_baseline,
                'Test_used': test_used,
                'p_value': p_value
            }

        return p_value < 0.05

    def fdr_correction(self, alpha=0.05):
        """Applies a global FDR correction for all tested categories in features, ranking them."""
        if not self._test_records:
            raise ValueError('No tests recorded yet.')

        df = pd.DataFrame(self._test_records.values())

        # Applying BH FDR across features

        reject, q_values, _, _ = multipletests(df['p_value'], alpha=alpha, method='fdr_bh')

        df['fdr_q'] = q_values
        df['FDR Significant'] = np.where(reject, 'True', 'False')
        
        return df.sort_values(by='fdr_q').reset_index(drop=True)

def plot_claims_imbalance(df, col='FraudFound_P'):
    """100% stacked bar chart showing overall class imbalance for the target column."""
    groups = df[col].value_counts()
    counts = len(df)

    count_0, count_1 = groups.get(0, 0), groups.get(1, 0)
    pct_0, pct_1 = (count_0 / counts) * 100, (count_1 / counts) * 100

    sns.set_theme(style='white')
    fig, ax = plt.subplots(figsize=(5, 6))

    ax.bar([''], [pct_0], color='green', label='Legit (0)')
    ax.bar([''], [pct_1], bottom=[pct_0], color='red', label='Fraud (1)')

    ax.text(0, pct_0 / 2, f'{count_0} ({pct_0:.2f}%)',
            ha='center', va='center', color='black', fontweight='bold', fontsize=11)
    ax.text(0, pct_0 + pct_1 / 2, f'{count_1} ({pct_1:.2f}%)',
            ha='center', va='center', color='black', fontweight='bold', fontsize=11)

    ax.set_yticks([0, 20, 40, 60, 80, 100], labels=[f'{p}%' for p in range(0, 101, 20)])
    ax.set_xlabel('')
    ax.set_ylabel('Percentage', fontsize=12)
    ax.set_title('Claims Fraud Class Imbalance', fontsize=12, fontweight='bold', pad=15)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 0), title="Classification", ncol=2)


    plt.tight_layout()
    plt.close(fig)
    return fig

def explore_discrete_feature(df, feature_name, order=None, target='FraudFound_P', tracker=None):
    """Plots a 100% stacked bar chart for features with discrete categories."""
    df = df

    # Defining the global baseline rate
    global_baseline = df[target].mean()

    # Defining fraud rate of each category in the feature for appropriate ordering
    fraud_rate = df.groupby(feature_name)[target].mean()
    feature_categories = df[feature_name].squeeze().unique()

    # Accounting for possible inputs for plot order
    if order is not None:
        supplied_order = list(order[feature_name]) if isinstance(order, dict) else list(order)
        final_order = [c for c in supplied_order if c in feature_categories]
    else:
        final_order = list(fraud_rate.sort_values(ascending=False).index)

    # defining feature categories' counts
    counts = df.groupby(feature_name)[target].agg(['sum','count']).copy()
    counts.columns = ['fraud_count', 'cell_total']
    counts['cell_fraud_rate'] = counts['fraud_count'] / counts['cell_total']
    counts = counts.reindex(final_order)

    # Instantiating lists for local test results
    test_used = []
    p_values = []
    verdicts = []

    # Iterating statistical tests
    for category, row in counts.iterrows():
            x_val = int(row['fraud_count'])
            n_val = int(row['cell_total'])
    
            expected_fraud = n_val * global_baseline
    
            if expected_fraud < 10:
                res = stats.binomtest(x_val, n=n_val, p=global_baseline, alternative='greater')
                p_val = res.pvalue
                test_used.append('Exact Binomial')
            else:
                p_val = stats.poisson.sf(x_val - 1, mu=expected_fraud)
                test_used.append('Poisson Approximation')
    
            # Tracking test results with the eda registry
            is_raw_sig = tracker.test_log(
                feature_name=feature_name,
                category=category,
                fraud_count=x_val,
                cell_total=n_val,
                local_fraud_rate=row['cell_fraud_rate'],
                expected_fraud= expected_fraud,
                global_baseline=global_baseline,
                test_used=test_used[-1],
                p_value=p_val
            )
            # Appending p_val, verdicts for each test
            verdicts.append('True' if is_raw_sig else '--')
            p_values.append(p_val)


    # Assembling Local Summary Table
    table = pd.DataFrame({
            'n': counts['cell_total'],
            'fraud_count': counts['fraud_count'],
            'legit_count': counts['cell_total'] -  counts['fraud_count'],
            'fraud_rate_pct': (counts['cell_fraud_rate'] * 100).round(2),
            'legit_rate_pct': (100 - (counts['cell_fraud_rate'] * 100)).round(2),
            'expected_fraud': (global_baseline * counts['cell_total']).round(),
            'test_used': test_used,
            'p_value': p_values,
            'is_flagged': verdicts
        })
    
    # Plotting function
    # Plotting function
    fig, ax = plt.subplots(figsize=(8,6))
    plot_table = table.iloc[::-1]

    y = np.arange(len(plot_table))
    ax.barh(y, plot_table['fraud_rate_pct'], label='Fraud', color='red', height=0.5)
    ax.barh(y, plot_table['legit_rate_pct'], left=plot_table['fraud_rate_pct'],label='Legitimate', color='green', height=0.5)
    # vertical line for the global baseline

    global_baseline_pct = global_baseline * 100
    ax.axvline(global_baseline_pct, color='black', linestyle='--', linewidth=2)
    
    ax.set_ylabel(feature_name)                              
    ax.set_xlabel('Percentage (%)')
    ax.set_yticks(y)
    ax.set_yticklabels(plot_table.index.astype(str))
    ax.set_xlim(0, 100)                    
    ax.set_title(f'Fraud Rate Composition across {feature_name}', fontweight='bold')
                          

    # Custom legend placed underneath the chart
    legit_patch = mpatches.Patch(color='green', label='Legit (0)')
    fraud_patch = mpatches.Patch(color='red', label='Fraud (1)')
    threshold_line = mlines.Line2D([],[], color='black', linestyle='--', linewidth=2, label=f'Global Fraud Rate ({global_baseline_pct:.2f}%)')
    ax.legend(handles=[legit_patch, fraud_patch, threshold_line], loc="upper center", 
            bbox_to_anchor=(0.5, -0.15), title="Legend", ncol=3)

    plt.tight_layout()

    return fig, table

def plot_continuous_class(df, col, target='FraudFound_P'):
    """KDE comparing the shape of col's distribution between fraud/legit classes.
    common_norm=False so each class's curve integrates independently, preventing
    the minority (fraud) class from appearing artificially flattened."""
    fig, ax = plt.subplots()
    sns.kdeplot(
        data=df, x=col, hue=target, common_norm=False,
        ax=ax, palette={0: 'green', 1: 'red'}
    )
    ax.set_title(f'{col} distribution by fraud status')

    legend = ax.get_legend()
    if legend:
        legend.set_title('Classification')
        for text, label in zip(legend.get_texts(), ['Legit (0)', 'Fraud (1)']):
            text.set_text(label)
    
    plt.close(fig)
    return fig
