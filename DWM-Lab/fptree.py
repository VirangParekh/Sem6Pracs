import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
# Load the dataset from excel sheet
df = pd.read_excel(
    'http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx')
# Data cleaning Process
# Remove extra spaces in the description part of the data
df['Description'] = df['Description'].str.strip()
# Drop the rows that are without Invoice Number
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
# Remove the credit transactions (Credit transactions contain 'C')
df = df[~df['InvoiceNo'].str.contains('C')]
# consolidate the items into 1 transaction per row with each product 1 hot encoded.
'''
Hot encoding, the basic strategy is to convert each category value into a new column and assigns a 1 or 0 (True/False) value to the column
'''
# We will look for the sales of France
basket = (df[df['Country'] == "France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))
'''
The lots of zeros in the dataset. We need to make sure that all positive numbers are converted to 1 and others are 0
we create a function for that named encode_units which returns 1 for all positive numbers and 0 otherwise.
'''


def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


# To make the data structured.
basket_sets = basket.applymap(encode_units)
# This step will complete the one hot encoding of the data and remove the postage column (since that charge is not one we wish to explore).
basket_sets.drop('POSTAGE', inplace=True, axis=1)
# Get the frequent item sets using fp tree with minimum support 0.07 and column names as items
frequent_itemsets = fpgrowth(basket_sets, min_support=0.07, use_colnames=True)
print(frequent_itemsets)
# Get the association rules based on the fp tree generated frequent item sets
rules = association_rules(
    frequent_itemsets, metric="confidence", min_threshold=0.7)
rules[(rules['lift'] >= 6) &
      (rules['confidence'] >= 0.8)]
