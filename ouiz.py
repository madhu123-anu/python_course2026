from pypdf import PdfReader
from gtts import gTTS

reader = PdfReader("C://Users//madhu/Downloads//Functions_Quiz-2.pdf")

full_text = ""

for page in reader.pages:
    content = page.extract_text()
    if content:
        full_text += content

tts = gTTS(text=full_text, lang="en")
tts.save("output.mp3")

        