import pandas as pd
from fpdf import FPDF

# Function to load and analyze the data
def analyze_data(file_path):
    try:
        # Read data from CSV
        data = pd.read_csv(file_path)
        summary = data.describe()  # Get summary statistics of numeric data
        return summary
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Function to generate PDF report
def generate_pdf_report(summary, output_file):
    pdf = FPDF()
    pdf.add_page()
    
    # Add title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Automated Data Report", ln=True, align="C")
    
    # Add summary statistics
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)  # Line break
    pdf.cell(200, 10, txt="Summary Statistics:", ln=True)
    
    # Convert summary dataframe to string and add to the PDF
    pdf.multi_cell(0, 10, txt=summary.to_string())
    
    # Save PDF
    pdf.output(output_file)
    print(f"Report generated: {output_file}")

# Main function to read the file, analyze data, and generate a report
if __name__ == "__main__":  # Fixed the typo here
    input_file = r"E:\klrahul\JAHNAVI\data.csv"  # Path to your CSV file
    output_file = "report.pdf"  # Output PDF file
    
    # Analyze data
    summary = analyze_data(input_file)
    if summary is not None:
        # Generate PDF report
        generate_pdf_report(summary, output_file)
    else:
        print("Data analysis failed. Report not generated.")
