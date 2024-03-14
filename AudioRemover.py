from tkinter import *
import AudioEditing
from tkinter import filedialog
root = Tk()
root.title("Audio Remover")
root.geometry("270x100")
root.iconbitmap("my_icon.ico")

selectedFileName = "NA"

my_words = Label(root, text = 'Remove audio from a video by picking a file')
my_words.pack()


def openFileExplorer():
    #print ("I CLICKED THE BUTTON")
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Video files", "*.mp4*"), ("all files", "*.*")))
    # Change label contents
    #label_file_explorer.configure(text="File Opened: "+filename)
    selectedFileName = filename
    file_name = Label(root, text = selectedFileName)
    file_name.pack()

    #generate output filename
    outputFileName = selectedFileName[:-1]
    outputFileName = selectedFileName[:-2]
    outputFileName = selectedFileName[:-3]
    outputFileName = selectedFileName[:-4]

    AudioEditing.remove_audio(selectedFileName, outputFileName + "_NOAUDIO.mp4")

my_button = Button(root, text = 'Select File', command = openFileExplorer)
my_button.pack()

root.mainloop()


