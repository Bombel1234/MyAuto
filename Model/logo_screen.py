from Model.base_model import BaseScreenModel


class LogoScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.LogoScreen.logo_screen.LogoScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self.base = database
        self._data = None


    @property
    def data(self):
        self._data = self.base.cursor.execute("SELECT * FROM listAuto").fetchall()
        return self._data


    def data_table_auto(self, key) -> bool:
        all_auto = self.base.cursor.execute(f"SELECT key FROM listAuto WHERE key='{key}'").fetchall()
        if len(all_auto) < 1:
            return True
        return False

    def add_auto(self, marka, model, key):
        self.base.cursor.execute(f"INSERT INTO listAuto VALUES(?,?,?,?,?,?,?,?,?)",
                                 (marka, model, key, None, None, None, None, None, None))
        self.base.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {key}("
            f"data TEXT NOT NULL,"
            f"km INT NOT NULL,"
            f"cena INT NOT NULL,"
            f"work TEXT NOT NULL)"
        )

        self.base.connect.commit()

    def delete_auto(self, title_auto):
        name_table = title_auto.lower().replace(' ', '')
        self.base.cursor.execute(
            f"DELETE FROM listAuto WHERE key='{name_table}'"
        )
        self.base.cursor.execute(
            f"DROP TABLE IF EXISTS {name_table}"
        )
        self.base.connect.commit()

    def edit_name_auto(self, now_marka, now_model, name_table):
        key = now_marka.lower().replace(' ', '') + now_model.lower().replace(' ', '')
        self.base.cursor.execute(
            f"UPDATE listAuto SET marka='{now_marka}', "
            f"model='{now_model}',"
            f"key='{key}' WHERE key='{name_table}'"
        )
        self.base.cursor.execute(
            f"ALTER TABLE {name_table}  RENAME TO {key}"
        )
        self.base.connect.commit()

    def select_all_table(self):
        res = self.base.cursor.execute("SELECT name FROM sqlite_master").fetchall()
        list_auto = [i[0] for i in res]
        return list_auto
