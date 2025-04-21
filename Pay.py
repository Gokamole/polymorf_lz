import pandas as pd
class Payment:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

    def __pos__(self):
        initial_count = len(self.df)
        self.df = self.df.drop_duplicates()
        removed_count = initial_count - len(self.df)
        print(f"Количество повторяющихся строк в наборе данных: {removed_count}")
        
    def split_by_year(self):
        self.df['Дата оплаты'] = pd.to_datetime(self.df['Дата оплаты'])
        self.df['Год'] = self.df['Дата оплаты'].dt.year
        self.data_before = self.df[self.df['Год'] < 2014]
        self.data_after = self.df[self.df['Год'] >= 2014]
        self.data_before.to_csv("data_before_2014.csv", index=False)
        self.data_after.to_csv("data_after_2014.csv", index=False)
        print(f"Данные сохранены")
