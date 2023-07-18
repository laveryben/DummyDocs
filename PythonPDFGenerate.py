import pandas as pd
import pdfplumber
from random import sample

# Load CSV into DataFrame
data_frame = pd.read_csv('Drinkslines.csv')

# Select random sample of 7 lines
random_sample = data_frame.sample(n=7)

# Create a PDF document
pdf = pdfplumber.PDF()

# Iterate over the selected lines and add them to the PDF
for index, row in random_sample.iterrows():
    line_item_text = row['LineItemText']
    item_amount = row['ItemAmount']
    
    # Add text to the PDF
    pdf.add_page().draw_text(f"Line Item Text: {line_item_text}", x=10, y=10)
    pdf.add_page().draw_text(f"Item Amount: {item_amount}", x=10, y=30)

# Save the PDF document
pdf.save('output.pdf')

# Close the PDF document
pdf.close()
