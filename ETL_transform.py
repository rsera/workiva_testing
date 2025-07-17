# An example of using Python to transform general ledger data for financial reporting
# Lots of comments (and printing) for learning purposes

import pandas as pd

# changing options to view all columns on one line because it was truncating with "..." in my print statements as it got too wide
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)  # Increase width
pd.set_option('display.max_colwidth', None)  # Don't truncate long values

# In reality, this would likley be pulled from a data source, but I'm hardcoding it here to have some sample values to work with without access to a database full of reporting data
rawData = {
    "Account": [462462, 211200, 256240],
    "Amount": [-45678.91, -15000.00, -10000.00],
    "Type": ["Revenue", "Liability", "Liability"],
    "Date": ["2025-07-16", "2025-07-16", "2025-07-17"]
}

# load data into a pandas DataFrame object
data = pd.DataFrame(rawData)

# test print to view dataframe
print("Initial Data\n", data)

# In double-entry bookkeeping, revenue and liability are "credits" and are stored as negatives. Flip the sign to make them positive for reporting
# this adds a new column to dataframe for the absolute values
data["Amount_absolute"] = data["Amount"].abs()

# test print
print("\nAbsolute column added\n", data)

# Dictionary to map Account numbers to descriptions
account_map = {
    462462: "Sales Revenue",
    211200: "Accounts Payable",
    256240: "Accrued Expenses"
}

# create a new column in the dataframe with the description for each account code
# map() is a pandas series method that loops through each entry in the series and applies a mapping dictionary
data["Account_Desc"] = data["Account"].map(account_map)

# test print to view dataframe with new column
print("\nDescription column added\n", data)

# perform date transformation using the pandas library to extract the year and month from the column named "Date" and add those new columns
data["Year"] = pd.to_datetime(data["Date"]).dt.year
data["Month"] = pd.to_datetime(data["Date"]).dt.month

# test print to view dataframe with new columns
print("\nYear and Month added\n", data)

# Grouping data by account type is a common task in ETL
# this sums the liabilities, etc and displays them by that type
grouped = data.groupby("Type")["Amount_absolute"].sum().reset_index()

# test print to view data after grouping
print("\nGrouped Data\n", grouped)

# add colutmn for original amount (non-absolute values) for audit trail
data["Original_Amount"] = data["Amount"]  

# test print to view dataframe with new columns
print("\nFinal with original amount\n", data)

# output to CSV
data.to_csv("output.csv", index=False)
