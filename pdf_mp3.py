from fpdf import FPDF

text_data = """Short Story: The Lazy Boy Who Changed

Ravi was a lazy boy. He loved sleeping and wasting time on his phone. Every day, he planned to study, but he never started.

One day, his teacher said, "Your future depends on what you do today."

That sentence hit him hard.

The next morning, Ravi woke up early. He studied for just one hour. It was not much, but it was a start.

Days passed, and Ravi slowly improved. He became more focused and confident.

At the end of the year, Ravi passed with good marks.

He smiled and said,
"Change doesn’t happen in one day, but it starts in one day."

Moral:
Start small, but start today.
"""

text_data = text_data.replace("’", "'")
text_data = text_data.replace("“", '"')
text_data = text_data.replace("”", '"')

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.multi_cell(0, 10, text_data)
pdf.output("story.pdf")

print("PDF created successfully!")



# from pypdf import PdfReader
# from gtts import gTTS
# import os
# pdf_path = "C:\\madhuri\\ebook\\story.pdf"
# if not os.path.exists(pdf_path):
#     print(" PDF file not found.")
# else:
#     reader = PdfReader(pdf_path)
#     full_text = ""
#     for page in reader.pages:
#         content = page.extract_text()
#         if content:
#             full_text += content + "\n"
#     if full_text.strip() == "":
#         print(" No text found in PDF.")
#     else:
#         print("Text extracted successfully!")
#         tts = gTTS(text=full_text, lang="en")
#         tts.save("story_audio.mp3")

#         print(" MP3 file created: story_audio.mp3")

        
from pypdf import PdfReader
from gtts import gTTS

reader = PdfReader("C:\\madhuri\\ebook\\story.pdf")

full_text = ""

for page in reader.pages:
    content = page.extract_text()
    if content:
        full_text += content

tts = gTTS(text=full_text, lang="en")
tts.save("story_audio.mp3")
