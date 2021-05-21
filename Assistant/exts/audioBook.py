import pyttsx3
import PyPDF2                                                                               # noqa
import os
# from constants import Client


def audioBook(pdfPath, fromPageNo=0):
    """ Funtion to read the pdf and save the audio in a mp3 file at the same directory where the pdf locatied """
    full_Text = str()
    with open(pdfPath, "rb") as book:
        reader = PyPDF2.PdfFileReader(book)
        audio_reader = pyttsx3.init('sapi5')
        audio_reader.setProperty("rate", 170)
        # audio_reader.setProperty("voice", Client.voices[Client.voice-1])
        
        for page in range(reader.numPages-fromPageNo):
            next_page = reader.getPage(page+fromPageNo)
            content = next_page.extractText()
            full_Text+=content
            

        audio_reader.save_to_file(content, os.path.join(pdfPath))
        audio_reader.runAndWait()

    

if __name__ == "__main__":
    audioBook(r"Assistant\media\Machine Learning.pdf", 23)