from __future__ import annotations
import sqlite3
from kivy.utils import platform


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """
    name = "baza_auto.db"

    def __init__(self):
        if platform == 'win':
            self.connect = sqlite3.connect(self.name)
            self.cursor = self.connect.cursor()
            self.create_table_auto()
            self.create_table_settings()
        else:
            from android import mActivity
            context = mActivity.getApplicationContext()
            self.result = context.getExternalFilesDir(None)
            self.storage_path = str(self.result.toString())
            self.connect = sqlite3.connect(f'{self.storage_path}/baza_auto.db')
            self.cursor = self.connect.cursor()
            self.create_table_auto()
            self.create_table_settings()
    
    def create_table_auto(self):
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS listAuto(
                            marka TEXT NOT NULL,
                            model TEXT NOT NULL,
                            key TEXT NOT NULL,
                            data_kupno TEXT,
                            data_sprzedaz TEXT,
                            cena TEXT,
                            color TEXT,
                            numer_rejes TEXT,
                            img TEXT
                        )
                        ''')
        self.connect.commit()

    def create_table_settings(self):
        self.cursor.execute('''
                                CREATE TABLE IF NOT EXISTS settings(
                                    theme TEXT NOT NULL,
                                    palette TEXT NOT NULL 
                                )
                                ''')
        self.connect.commit()

    def all_settings(self):
        setting = self.cursor.execute("""
        SELECT * FROM settings
        """).fetchall()
        return setting

    def add_default_settings(self, a, b):
        self.cursor.execute("""
        INSERT INTO settings VALUES(?,?)
        """, (a, b))
        self.connect.commit()
