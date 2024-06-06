from fpdf import FPDF

pdf = FPDF(orientation="p",unit="mm",format="a4")
pdf.add_page()

pdf.output("output.pdf")