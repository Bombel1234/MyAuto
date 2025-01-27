"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import ScreenManager, NoTransition

from View.screens import screens
from Model.database import DataBase

from kivy.core.window import Window

from android import mActivity

Window.softinput_mode = 'below_target'


class AutoBook(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.quit_app)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager(transition=NoTransition())
        self.database = DataBase()

    def quit_app(self, window, key, *args):
        if key == 27:
            mActivity.finishAndRemoveTask()
            return True
        else:
            return False

    def build(self) -> MDScreenManager:
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.material_style = 'M2'
        self.generate_application_screens()
        self.open_settings_table()
        return self.manager_screens

    def open_settings_table(self):
        all_in_settings = self.database.all_settings()
        if len(all_in_settings) < 1:
            a = self.theme_cls.theme_style
            b = self.theme_cls.primary_palette
            self.database.add_default_settings(a, b)
        else:
            data_from_settings = self.database.all_settings()
            self.theme_cls.theme_style = data_from_settings[0][0]
            self.theme_cls.primary_palette = data_from_settings[0][1]

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"](self.database)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


AutoBook().run()
