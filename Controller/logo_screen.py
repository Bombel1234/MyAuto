from View.LogoScreen.components import ListItem
from View.LogoScreen.logo_screen import LogoScreenView


class LogoScreenController:
    """
    The `LogoScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.logo_screen.LogoScreenModel
        self.view = LogoScreenView(controller=self, model=self.model)

    def get_view(self) -> LogoScreenView:
        return self.view

    def move_to_screen_settings(self):
        self.view.manager_screens.current = 'settings screen'

    def add_auto(self, button, obj):
        if obj.ids.marka.text != '' and obj.ids.model.text != '':
            marka = obj.ids.marka.text
            model = obj.ids.model.text
            key = str(marka).lower().replace(' ', '') + str(model).lower().replace(' ', '')
            if self.model.data_table_auto(key):
                self.model.add_auto(marka, model, key)
                self.view.add_object(obj)
            else:
                self.view.open_dialog_is_auto()
        self.view.close_dialog_add_auto()



    def list_auto(self):
        list_auto = self.model.data
        return list_auto

    def click_auto_from_list(self, instance: ListItem):
        self.view.manager_screens.get_screen('home screen').ids.title_screen.title = str(instance.text).upper()
        self.view.parent.current = 'home screen'

    def delete_item(self, button):
        title_auto = button.parent.parent.text
        obj_item = button.parent.parent
        self.view.delete_auto_dialog(title_auto, obj_item)

    def delete(self, button, title_auto, t):
        self.model.delete_auto(title_auto)
        self.view.delete_widget(t)
        self.view.close_dialog()

    def click_edit(self, button):
        title_item = button.parent.parent.text
        obj_item = button.parent.parent
        self.view.open_dialog_edit(title_item, obj_item)

    def edit(self, button, obj_listItem, now_marka, now_model, marka, model):
        name_table_stare = marka.lower().replace(' ', '') + model.lower().replace(' ', '')
        name_table_now = now_marka.lower().replace(' ', '') + now_model.lower().replace(' ', '')
        res = self.model.select_all_table()
        if not name_table_now in res:
            obj_listItem.text = f"{now_marka} {now_model}"
            self.model.edit_name_auto(now_marka, now_model, name_table_stare)
        self.view.close_dialog_edit()
