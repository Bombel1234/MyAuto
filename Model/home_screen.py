from Model.base_model import BaseScreenModel


class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.HomeScreen.home_screen.HomeScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self.base = database
        self._data = None

    def add_info_auto(self, name_table, data, km, cena, work):
        self.base.cursor.execute(
            f"INSERT INTO {name_table} VALUES(?,?,?,?)",
            (data, km, cena, work)
        )
        self.base.connect.commit()

    def data_info(self, name_table):
        res = self.base.cursor.execute(
            f"SELECT * FROM {name_table}"
        ).fetchall()
        return res

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        # We notify the View -
        # :class:`~View.HomeScreen.home_screen.HomeScreenView` about the
        # changes that have occurred in the data model.
        self.notify_observers("home screen")

    def edit_card_info(self, data_dict):
        name_table = data_dict['name_table']

        data_ = data_dict['stare_value']['data']
        km_ = data_dict['stare_value']['km']
        cena_ = data_dict['stare_value']['cena']
        work_ = data_dict['stare_value']['work']

        data = data_dict['now_value']['data']
        km = data_dict['now_value']['km']
        cena = data_dict['now_value']['cena']
        work = data_dict['now_value']['work']

        self.base.cursor.execute(
            f"UPDATE {name_table} SET data='{data}', km='{km}', cena='{cena}',"
            f"work='{work}' WHERE data='{data_}' AND km='{km_}' AND cena='{cena_}'"
            f"AND work='{work_}'"
        )
        self.base.connect.commit()

    def add_data_kupno(self, name_table, content):
        self.base.cursor.execute(
            f"UPDATE listAuto SET data_kupno='{content}'"
            f"WHERE key='{name_table}'"
        )
        self.base.connect.commit()

    def add_data_sprzedash(self, name_table, content):
        self.base.cursor.execute(
            f"UPDATE listAuto SET data_sprzedaz='{content}'"
            f"WHERE key='{name_table}'"
        )
        self.base.connect.commit()

    def add_data_cena(self, name_table, content):
        self.base.cursor.execute(
            f"UPDATE listAuto SET cena='{content}'"
            f"WHERE key='{name_table}'"
        )
        self.base.connect.commit()

    def add_data_color(self, name_table, content):
        self.base.cursor.execute(
            f"UPDATE listAuto SET color='{content}'"
            f"WHERE key='{name_table}'"
        )
        self.base.connect.commit()

    def add_data_numer(self, name_table, content):
        self.base.cursor.execute(
            f"UPDATE listAuto SET numer_rejes='{content}'"
            f"WHERE key='{name_table}'"
        )
        self.base.connect.commit()

    def select_info_bottom(self, key):
        res = self.base.cursor.execute(
            f"SELECT  data_kupno, data_sprzedaz, cena, color,"
            f"numer_rejes, img FROM listAuto WHERE key='{key}'"
        ).fetchall()
        return res

    def suma_inwest(self, name_table):
        suma = self.base.cursor.execute(
            f"SELECT SUM(cena) FROM {name_table}"
        ).fetchone()
        return suma[0]


    def update_path_to_image(self, path, key):
        self.base.cursor.execute(
            f"UPDATE listAuto SET img='{path}'"
            f"WHERE key='{key}'"
        )
        self.base.connect.commit()



