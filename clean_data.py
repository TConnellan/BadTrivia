import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('./Trivia-Printable.xlsx')

# Create new DataFrame with the combined columns
new_df = pd.DataFrame({
    df.columns[0]: list(df.iloc[1:, 0]) + list(df.iloc[1:, 3]) + list(df.iloc[1:, 6]),
    df.columns[1]: list(df.iloc[1:, 1]) + list(df.iloc[1:, 4]) + list(df.iloc[1:, 7]),
})

# Remove rows where either column has empty strings
new_df = new_df.fillna('')
new_df = new_df[
    new_df[new_df.columns[0]].str.strip().astype(bool) &  # Non-empty, non-whitespace in column 0
    new_df[new_df.columns[1]].str.strip().astype(bool)   # Non-empty, non-whitespace in column 1
]

# Save the updated DataFrame as a CSV
new_df.to_csv('updated_file.csv', index=False)