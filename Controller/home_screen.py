from urllib.parse import urljoin
import requests

from View.HomeScreen.home_screen import HomeScreenView


class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = HomeScreenView(controller=self, model=self.model)

    def get_view(self) -> HomeScreenView:
        return self.view

    def back_screen(self):
        self.view.manager_screens.current = 'logo screen'

    def add_info(self, btn, content_info, name_table, dd, mm, yy):
        km = content_info.ids.km_.text
        cena = content_info.ids.cena_.text
        work = content_info.ids.work_.text

        if km != '' and cena != '' and work != '':
            data = f"{dd}/{mm}/{yy}"
            self.model.add_info_auto(
                name_table.lower().replace(' ', ''),
                data, km, cena, work
            )
            self.view.add_object(content_info, data)
        self.view.close_dialog_add_info()

    def select_data_info(self, name_table):
        res = self.model.data_info(name_table)
        return res

    def edit_info(self, x, content, obj_card, name_table, stare_data):
         # nowe_value value
        data_ = content.ids.data_.text
        km_ = content.ids.km_.text
        work_ = content.ids.work_.text
        cena_ = content.ids.cena_.text

        dict_data = {
            "name_table": name_table,
            "stare_value": {
                "data": stare_data[0],
                "km": stare_data[1],
                "cena": stare_data[2],
                "work": stare_data[3]
            },
            "now_value": {
                "data": data_,
                "km": km_,
                "cena": cena_,
                "work": work_
            }
        }
        data_edit = [data_, km_, cena_, work_]
        self.view.edit_object(obj_card, data_edit)
        self.model.edit_card_info(dict_data)
        self.view.close_dialog_edit()


    def data_plus_auto(self, btn, name_table, text, obj, content) -> None:
        self.view.close_dialog_info_bottom()
        match text:
            case 'Data kupna auto':
                if content != '':
                    self.model.add_data_kupno(name_table, content)
                    obj.text = content
            case 'Data sprzedazy auto':
                if content != '':
                    self.model.add_data_sprzedash(name_table, content)
                    obj.text = content
            case 'Cena auto':
                if content != '':
                    self.model.add_data_cena(name_table, content)
                    obj.text = content
            case 'Kolor auto':
                if content != '':
                    self.model.add_data_color(name_table, content)
                    obj.text = content
            case 'Numer rejestracyjny':
                if content != '':
                    self.model.add_data_numer(name_table, content)
                    obj.text = content

    def click_add_img(self, btn, path_to_img, key_auto):
        if path_to_img != '':
            first_url = "https://google.com"
            final_url = urljoin(first_url, path_to_img)
            if requests.get(final_url).status_code == 200:
                self.model.update_path_to_image(path_to_img, key_auto)
                self.view.add_img(path_to_img)
            else:
                self.view.error_image()
        self.view.close_dialog_add_image()