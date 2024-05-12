import PySimpleGUI as sg


label_1 = sg.Text("Select file to compress")
input_1 = sg.Input()
button_1 = sg.FilesBrowse("Choose")
label_2 = sg.Text("Select destination folder")
input_2 = sg.Input()
button_2 = sg.FilesBrowse("Choose")
button_3 = sg.Button("Compress")


window = sg.Window("File Compresses",
                   [[label_1, input_1, button_1],
                    [label_2, input_2, button_2],
                    [button_3]])
window.read()
window.close()
