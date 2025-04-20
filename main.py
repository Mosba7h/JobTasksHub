import argparse
from reporter import generate_insights, generate_report
from pdf_generator import PDFGenerator
import os

def main():
    parser = argparse.ArgumentParser(description="Autonomous Industry Intelligence Report Generator")
    parser.add_argument('query', help='Business-level query to generate report for')
    parser.add_argument('--pdf', default='report.pdf', help='Output PDF filename')
    args = parser.parse_args()

    try:
        insights = generate_insights(args.query)
        report_md = generate_report(insights, args.query)

        md_filename = os.path.splitext(args.pdf)[0] + '.md'

        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(report_md)

        pdf = PDFGenerator(args.pdf)
        pdf.write_markdown(report_md)
        pdf.save()

        print(f"✔ Report generated: {md_filename} and {args.pdf}")

    except Exception as e:
        print(f"❌ Error generating report: {str(e)}")

if __name__ == '__main__':
    main()
    