from Model.base_model import BaseScreenModel


class SettingsScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SettingsScreen.settings_screen.SettingsScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self._data = None
        self.base = database
        self.primary = ['BlueGray', 'Amber', 'DeepOrange', 'DeepPurple',
                        'Red', 'Pink', 'Purple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal',
                        'Green', 'LightGreen',
                        'Lime', 'Yellow', 'Orange', 'Brown', 'Gray',
                        ]

        self.color = ['#617D8C', '#FFC208', '#FF5721', '#6638B5', 'red', 'pink', 'purple', 'indigo',
                      'blue', 'lightblue', 'cyan', 'teal', 'green', 'lightgreen',
                      'lime', 'yellow', 'orange', 'brown', 'gray']

    def select_palette_color(self, color_palette):
        self.base.cursor.execute(
            f"UPDATE settings SET palette='{color_palette}'"
        )
        self.base.connect.commit()

    def theme_select(self, color_theme):
        self.base.cursor.execute(
            f"UPDATE settings SET theme='{color_theme}'"
        )
        self.base.connect.commit()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.SettingsScreen.settings_screen.SettingsScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("settings screen")
