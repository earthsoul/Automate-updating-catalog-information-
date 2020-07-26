#!/usr/bin/env python3  # shebang

from reportlab.platypus import SimpleDocTemplate  # used to generate PDFs
from reportlab.platypus import Paragraph, Spacer, Table, Image  # flowables
from reportlab.lib.styles import getSampleStyleSheet  # used for document styles
from reportlab.lib import colors  # used for table styles

def generate(filename, title, additional_info):  # function to generate PDF
  styles = getSampleStyleSheet()  # sample dictionary of various styling
  report = SimpleDocTemplate(filename)  # export directory and filename
  report_title = Paragraph(title, styles["h1"])  # title style
  report_info = Paragraph(additional_info, styles["BodyText"])  # body style
  report.build([report_title, report_info]) 
