import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('input.pdf', 'rb'))
speaker = pyttsx3.init()

clean_text = ""

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'output.mp3')
speaker.runAndWait()

speaker.stop()
