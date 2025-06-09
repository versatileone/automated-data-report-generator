from fpdf import FPDF
import csv
import pandas as pd

#reading a csv file data

data=pd.read_csv("age.csv")
summary=data.describe()
total_rows=len(data)
# initialising a pdf

pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=12)

# adding tile
pdf.cell(200,10,txt="automated data report",ln=True,align="C")
pdf.ln(10)

# total rows
pdf.cell(200,10,txt=f"total rows:{total_rows}",ln=True,align="C")

# summerized table
pdf.ln(5)
pdf.set_font("Arial",size=10)
for col in summary.columns:
    pdf.cell(200,10,txt=f"column :{col}",ln=True)
    stats=summary[col].to_dict()
    for stat,values in stats.items():
        pdf.cell(200,10,txt=f"{stat}:{values}",ln=True)
pdf.output("data_report.pdf")
    