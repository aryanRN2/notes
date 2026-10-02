import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
import subprocess

# List of 69 M1 Students extracted accurately from the image
students_m1 = [
    # Top table (1-32)
    ("24229MAT002", "Anchal Singh KANWAR"),
    ("24229MAT003", "Anjali Kharwar"),
    ("24229MAT004", "Anju Saroj"),
    ("24229MAT005", "Anushka Singh"),
    ("24229MAT007", "Ayushi Gupta"),
    ("24229MAT008", "Chandani Sonkar"),
    ("24229MAT009", "Deepika Dubey"),
    ("24229MAT010", "Deeptanshi Yadav"),
    ("24229MAT011", "Divyanshi Verma"),
    ("24229MAT012", "Kamlini Singh"),
    ("24229MAT013", "Kaushilya"),
    ("24229MAT014", "Khyati Chaubey"),
    ("24229MAT015", "Komal Kumari"),
    ("24229MAT016", "Kumari Bhumi Sharma"),
    ("24229MAT017", "Mini Yadav"),
    ("24229MAT018", "Mithu Kumari"),
    ("24229MAT019", "Monika Bagriya"),
    ("24229MAT020", "Palak"),
    ("24229MAT021", "Prachi"),
    ("24229MAT022", "Pragya Yadav"),
    ("24229MAT023", "Purvi Jethwa"),
    ("24229MAT024", "Roshani Kumari"),
    ("24229MAT025", "Sakshi Gautam"),
    ("24229MAT026", "Samriddhi Kumari"),
    ("24229MAT028", "Shraddha Verma"),
    ("24229MAT029", "Shubhi Shukla"),
    ("24229MAT030", "Shweta Pandey"),
    ("24229MAT031", "Suman Jaiswal"),
    ("24229MAT032", "Vandana Maurya"),
    ("24229MAT033", "Vijeta Kumari"),
    ("24220MAT003", "Aayushi Singh"),
    ("24220MAT004", "Abdul Mustakeem"),
    # Bottom table (33-69)
    ("24220MAT005", "Abhinav Pal"),
    ("24220MAT006", "Abhishek Gupta"),
    ("24220MAT007", "Abhishek Kumar"),
    ("24220MAT008", "Abhishek Kumar"),
    ("24220MAT009", "Abhishek Meena"),
    ("24220MAT010", "Abhishek Rajput"),
    ("24220MAT012", "Achal Kumar"),
    ("24220MAT013", "Adarsh Kumar"),
    ("24220MAT014", "Adarsh Pathak"),
    ("24220MAT015", "Aditi Kumari"),
    ("24220MAT016", "Aditya Pandey"),
    ("24220MAT017", "Aditya Patel"),
    ("24220MAT019", "Aditya Yadav"),
    ("24220MAT021", "Akash Rai"),
    ("24220MAT022", "Akhilesh Yadav"),
    ("24220MAT023", "Akshatra Dev Upadhyay"),
    ("24220MAT024", "Akshit Agarwal"),
    ("24220MAT028", "Amandeep"),
    ("24220MAT029", "Ambuj Singh"),
    ("24220MAT032", "Aniket Ray"),
    ("24220MAT033", "Aniket Verma"),
    ("24220MAT034", "Anjali Kumari"),
    ("24220MAT035", "Ankesh Dhakar"),
    ("24220MAT036", "Ankit Kumar Yadav"),
    ("24220MAT038", "Ankit Yadav"),
    ("24220MAT039", "ANKITA MONDAL"),
    ("24220MAT040", "Ankush Lodhi"),
    ("24220MAT041", "Anmol Tiwari"),
    ("24220MAT042", "Anshika Mishra"),
    ("24220MAT044", "Anshuman Singh"),
    ("24220MAT045", "Anushka Nandy"),
    ("24220MAT046", "Anvisha Yadav"),
    ("24220MAT049", "Arya Tripathi"),
    ("24220MAT051", "Aryan Maurya"),
    ("24220MAT052", "Ashana Maurya"),
    ("24220MAT053", "ASHISH KUMAR"),
    ("24220MAT055", "Asmita Maurya")
]

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8.5)
        self.setFillColor(colors.HexColor("#2563EB"))
        
        # Header
        self.drawString(36, 810, "sciqb.com")
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#4A5568"))
        self.drawString(95, 810, "|   B.Sc. (Hons.) Mathematics — Vth Semester (Session 2026-2027)")
        self.drawRightString(559, 810, "Section M1 Student Roll List")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.75)
        self.line(36, 802, 559, 802)
        
        # Footer
        self.line(36, 35, 559, 35)
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#2563EB"))
        self.drawString(36, 22, "sciqb.com")
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#4B5563"))
        self.drawString(90, 22, "|   Department of Mathematics | Institute of Science")
        self.drawRightString(559, 22, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf(filename="M1_Students_List.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=50,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15.5,
        leading=19,
        textColor=colors.HexColor("#1E3A8A"),
        alignment=1
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2563EB"),
        alignment=1
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#374151"),
        alignment=1
    )

    th_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=0
    )

    th_style_center = ParagraphStyle(
        'TableHeaderCenter',
        parent=th_style,
        alignment=1
    )

    td_sn_style = ParagraphStyle(
        'TableDataSN',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#1E3A8A"),
        alignment=1
    )

    td_roll_style = ParagraphStyle(
        'TableDataRoll',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#1F2937"),
        alignment=1
    )

    td_name_style = ParagraphStyle(
        'TableDataName',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#111827"),
        alignment=0
    )

    story = []

    # Document Header
    story.append(Paragraph("Major — B.Sc. (Hons.) Vth Semester Session 2026–2027", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Group M1 — Complete Student Roll List", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>sciqb.com</b> &nbsp;&nbsp;|&nbsp;&nbsp; <b>Total Students: 69</b> &nbsp;&nbsp;|&nbsp;&nbsp; <i>Arranged with Serial Numbers (Original Order Preserved)</i>", meta_style))
    story.append(Spacer(1, 10))

    # Split into 2 side-by-side tables (35 in left, 34 in right)
    left_students = students_m1[:35]
    right_students = students_m1[35:]

    table_data = []

    # Header Row
    header_row = [
        Paragraph("S.No.", th_style_center),
        Paragraph("Exams Roll No.", th_style_center),
        Paragraph("Student Name", th_style),
        Paragraph("", th_style), # Divider
        Paragraph("S.No.", th_style_center),
        Paragraph("Exams Roll No.", th_style_center),
        Paragraph("Student Name", th_style)
    ]
    table_data.append(header_row)

    max_rows = max(len(left_students), len(right_students))

    for i in range(max_rows):
        row = []
        # Left side
        if i < len(left_students):
            sn = str(i + 1)
            roll, name = left_students[i]
            row.extend([
                Paragraph(sn, td_sn_style),
                Paragraph(roll, td_roll_style),
                Paragraph(name, td_name_style)
            ])
        else:
            row.extend(["", "", ""])

        # Divider column
        row.append("")

        # Right side
        if i < len(right_students):
            sn = str(i + 36)
            roll, name = right_students[i]
            row.extend([
                Paragraph(sn, td_sn_style),
                Paragraph(roll, td_roll_style),
                Paragraph(name, td_name_style)
            ])
        else:
            row.extend(["", "", ""])

        table_data.append(row)

    # Column widths: page width = 595 - 72 = 523pt
    # Col widths: Left [32, 78, 142], Sep [12], Right [32, 78, 149] -> Total = 523
    col_widths = [32, 78, 142, 12, 32, 78, 149]

    t = Table(table_data, colWidths=col_widths, repeatRows=1)

    t_style = [
        ('BACKGROUND', (0, 0), (2, 0), colors.HexColor("#1E3A8A")),
        ('BACKGROUND', (4, 0), (6, 0), colors.HexColor("#1E3A8A")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (2, -1), 0.4, colors.HexColor("#CBD5E1")),
        ('GRID', (4, 0), (6, -1), 0.4, colors.HexColor("#CBD5E1")),
    ]

    # Alternating row colors
    for r in range(1, len(table_data)):
        bg_color = colors.HexColor("#F8FAFC") if r % 2 == 1 else colors.white
        t_style.append(('BACKGROUND', (0, r), (2, r), bg_color))
        t_style.append(('BACKGROUND', (4, r), (6, r), bg_color))

    t.setStyle(TableStyle(t_style))
    story.append(t)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_pdf()
