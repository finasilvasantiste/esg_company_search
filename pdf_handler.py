from pypdf import PdfReader


def test():
	reader = PdfReader("esg_reports/microsoft_2022.pdf")
	number_of_pages = len(reader.pages)
	page = reader.pages[0]
	text = page.extract_text()

	print(number_of_pages)
	