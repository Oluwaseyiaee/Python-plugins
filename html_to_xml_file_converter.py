import pandas as pd

# Read HTML table into DataFrame
df_list = pd.read_html('filename.html')
df = df_list[0]  # Assuming the table is the first one in the HTML file

# Write DataFrame to Excel
df.to_excel('newFileName.xlsx', index=False)
