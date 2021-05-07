import PySimpleGUI as ui
import Analex as al

code_editor_column = [
    [
        ui.Text("Escriba el código aquí")
    ],

    [
        ui.Multiline(size=(50, 30), background_color="black", text_color="white", key="_CODE")
    ],

    [
        ui.Button("Analizar")
    ]
]

toke_list_column = [
    [
        ui.Text("Lista de tokens")
    ],
    [
        ui.Listbox(values=[], size=(50, 30), key="_LIST")
    ]
]

layout = [
    [
        ui.Column(code_editor_column),
        ui.VSeparator(),
        ui.Column(toke_list_column)
    ]
]

window = ui.Window("Analizador léxico", layout)

while True:
    event, values = window.read()
    if event == ui.WIN_CLOSED:
        break
    if event == "Analizar":
        code = values["_CODE"]
        la = al.LexicalAnalizer()
        tokens = la.AnalyzeCode(code)
        lexems = la.GetTokensValue()
        window["_LIST"].update(values=lexems)
window.close()
