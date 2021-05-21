import pyttsx3
import PyPDF2                                                                               # noqa
import os
from tkinter.filedialog import *

# from constants import Client


def audioBook(pdfPath=askopenfilename(), fromPageNo=0):
    """ Funtion to read the pdf and save the audio in a mp3 file at the same directory where the pdf locatied """
    full_Text = str()

    if ".pdf" not in pdfPath:       
        return None

    with open(pdfPath, "rb") as book:
        try:
            reader = PyPDF2.PdfFileReader(book)
            audio_reader = pyttsx3.init('sapi5')
            audio_reader.setProperty("rate", 170)
            # audio_reader.setProperty("voice", Client.voices[Client.voice-1])
            
            for page in range(fromPageNo, reader.numPages):
                next_page = reader.getPage(page)
                content = next_page.extractText()
                full_Text+=content
                
                
            audiofile = pdfPath.replace(".pdf", ".mp3")
            audio_reader.save_to_file(content, audiofile)
            audio_reader.runAndWait()
        except Exception:
            return None
    return audiofile
 


if __name__ == "__main__":
    # audioBook(r"M:\ADMIN\Critical Data\VS-Code\Alice\Assistant\media\Machine Learning.pdf", 23)
    audioBook()