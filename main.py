from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p",unit="mm",format="a4")
pdf.set_auto_page_break(auto=False, margin=0 )

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="l", ln=1)

    # To add many lines to the file
    # for y in range(20, 298, 10):
    #     pdf.line(10, y, 200, y)

    # Set Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # To add many lines to the file
        # for y in range(20, 298, 10):
        #     pdf.line(10, y, 200, y)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Set Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")