import PySimpleGUI as sg
from bonus import zip_creator

label_1 = sg.Text("Select file to compress")
input_1 = sg.Input()
choose_button_1 = sg.FilesBrowse("Choose", key="files")

label_2 = sg.Text("Select destination folder")
input_2 = sg.Input()
choose_button_2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

output_label = sg.Text(key="output", text_color="red")

window = sg.Window("File Compresses",
                   [[label_1, input_1, choose_button_1],
                    [label_2, input_2, choose_button_2],
                    [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    zip_creator.make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")

window.close()
