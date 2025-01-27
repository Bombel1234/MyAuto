from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.app import MDApp


class UpdateData(MDBoxLayout):
    day = StringProperty()
    month = StringProperty()
    year = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_list_item = []
        self.all_list_item_mm = []
        self.app = MDApp.get_running_app()
        self.data_dd = [
            '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
            '31'
        ]
        self.data_mm = [
            'Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj',
            'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień'
        ]
        self.create_box_date()

    def create_box_date(self):
        for i in self.data_dd:
            list_item = OneLineListItem(
                text=f"{str(i)}",
                on_press=lambda x: self.click_list_item_dd(x)
            )
            self.all_list_item.append(list_item)
            self.ids.container1.add_widget(list_item)
        for j in self.data_mm:
            list_item_mm = OneLineListItem(
                text=f"{str(j)}",
                on_press=lambda y: self.click_list_item_mm(y)
            )
            self.all_list_item_mm.append(list_item_mm)
            self.ids.container2.add_widget(list_item_mm)

    def click_list_item_dd(self, obj):
        self.ids.dd.text = obj.text
        for button in self.all_list_item:
            button.bg_color = [1, 1, 1, 0]
            obj.theme_text_color = 'Custom'
            if self.app.theme_cls.theme_style == 'Dark':
                button.text_color = (1, 1, 1, 1)
            else:
                button.text_color = (0, 0, 0, 1)
        obj.bg_color = (1, 0, 0, 1)
        obj.theme_text_color = 'Custom'
        obj.text_color = (0, 0, 0, 1)

    def click_list_item_mm(self, obj):
        self.ids.mm.text = obj.text
        for button in self.all_list_item_mm:
            button.bg_color = [1, 1, 1, 0]
            obj.theme_text_color = 'Custom'
            if self.app.theme_cls.theme_style == 'Dark':
                button.text_color = (1, 1, 1, 1)
            else:
                button.text_color = (0, 0, 0, 1)
        obj.bg_color = (1, 0, 0, 1)
        obj.theme_text_color = 'Custom'
        obj.text_color = (0, 0, 0, 1)