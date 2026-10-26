import flet as ft

import flet as ft
from view import View



class Controller():
    def __init__(self, model : Model, view : ft.View):
        self._model = model
        self._view = view

    def handler_minus(self, e):
        # print("-")
        # v = int(myText.value)
        # v = v - 1
        # myText.value = v
        # myText.update()
        self._model.valore -= 1
        # Dovrei dire alla view/page di aggiornarsi
        self._view.aggiorna_GUI()

    def handler_plus(self, e):
        # print("+")
        # v = int(myText.value)
        # v = v + 1
        # myText.value = v
        # myText.update()
        self._model.valore += 1
        # Dovrei dire alla view/page di aggiornarsi
        self._view.aggiorna_GUI()