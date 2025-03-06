from pypdf import PdfReader

reader = PdfReader('example.pdf')

print(len(reader.pages))

page =  reader.pages[0]

text = page.extract_text()
print(text)