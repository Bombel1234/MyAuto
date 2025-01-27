from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from View.LogoScreen.components import ListItem, ContentEdit, AddAuto  # NOQA
from View.base_screen import BaseScreenView


class LogoScreenView(BaseScreenView):
    dialog_add_auto = None
    dialog_delete_auto = None
    dialog_edit = None
    dialog_is_auto = None

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_pre_enter(self, *args):
        list_auto = self.controller.list_auto()
        self.add_auto_list(list_auto)

    def on_leave(self, *args):
        if self.ids.box_list_auto.children:
            self.ids.box_list_auto.clear_widgets()

    def create_box_list_auto(self, item):
        item_list = ListItem()
        item_list.text = f"{item[0]} {item[1]}"
        callback_list_delete = self.controller.delete_item
        item_list.ids.btn_delete.bind(on_release=lambda x: callback_list_delete(x))
        callback_list = self.controller.click_auto_from_list
        item_list.bind(on_release=lambda x: callback_list(x))
        callback_edit = self.controller.click_edit
        item_list.ids.btn_edit.bind(on_release=lambda x: callback_edit(x))
        self.ids.box_list_auto.add_widget(item_list)

    def add_auto_list(self, list_auto):
        for item in list_auto:
            self.create_box_list_auto(item)

    def add_auto(self):
        obj_add_auto = AddAuto()
        if not self.dialog_add_auto:
            self.dialog_add_auto = MDDialog(
                title="Dodawanie auta",
                type="custom",
                content_cls=obj_add_auto,
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog_add_auto
                    ),
                    MDFlatButton(
                        text="Dodaj",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.controller.add_auto(
                            x, obj_add_auto
                        )
                    ),
                ],
            )
        self.dialog_add_auto.open()

    def close_dialog_add_auto(self, *args):
        self.dialog_add_auto.dismiss()

    def add_object(self, obj):
        marka = obj.ids.marka.text
        model = obj.ids.model.text
        item_list = ListItem()
        item_list.text = f"{marka} {model}"
        callback_list_delete = self.controller.delete_item
        item_list.ids.btn_delete.bind(on_release=lambda x: callback_list_delete(x))
        callback_list = self.controller.click_auto_from_list
        item_list.bind(on_release=lambda x: callback_list(x))
        callback_edit = self.controller.click_edit
        item_list.ids.btn_edit.bind(on_release=lambda x: callback_edit(x))
        self.ids.box_list_auto.add_widget(item_list)

    def open_dialog_is_auto(self) -> None:
        self.dialog_is_auto = MDDialog(title='Juz jest take auto')
        self.dialog_is_auto.open()

    def delete_auto_dialog(self, title_auto, obj):
        if not self.dialog_delete_auto:
            self.dialog_delete_auto = MDDialog(
                title=f"Uwaga: Wykasowanie auto {title_auto}",
                text='I wszyskich danych',
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="Wstecz",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="Tak, wykasowac",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.controller.delete(x, title_auto, obj)
                    ),
                ],
            )
        self.dialog_delete_auto.open()

    def close_dialog(self, *args):
        self.dialog_delete_auto.dismiss()
        self.dialog_delete_auto = None

    def delete_widget(self, widget):
        self.ids.box_list_auto.remove_widget(widget)

    def open_dialog_edit(self, title_list, obj):
        marka_model = title_list.split(' ')
        marka = marka_model[0]
        model = marka_model[1]
        obj_edit = ContentEdit()
        obj_edit.text_marka = marka
        obj_edit.text_model = model
        if not self.dialog_edit:
            self.dialog_edit = MDDialog(
                title="Edytowanie auta",
                type="custom",
                content_cls=obj_edit,
                auto_dismiss=False,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press=self.close_dialog_edit
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda x: self.controller.edit(
                            x,
                            obj,
                            obj_edit.ids.input_marka.text,
                            obj_edit.ids.input_model.text,
                            marka,
                            model
                        )
                    ),
                ],
            )
        self.dialog_edit.open()

    def close_dialog_edit(self, *args):
        self.dialog_edit.dismiss()
        self.dialog_edit = None
