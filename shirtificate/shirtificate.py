from fpdf import FPDF

class Shirtificate:
    def __init__(self, name: str):
        self.name = name

    def generate(self, filename: str = "shirtificate.pdf"):
        pdf = FPDF(orientation='portrait', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial", size=60)
        pdf.cell(0, 30, "CS50 Shirtificate", ln=True, align='C')
        pdf.image("shirtificate.png", x=0, y=50)
        pdf.set_font("Arial", size=30)
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 185, f"{self.name} took CS50", ln=True, align='C')
        pdf.ln(10)
        pdf.output(filename)

if __name__ == "__main__":
    name = input("Enter your name: ")
    shirtificate = Shirtificate(name)
    shirtificate.generate()
