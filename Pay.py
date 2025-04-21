import pandas as pd
class Payment:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

    def copy(self):
        key = ['Участники гражданского оборота','Тип операции','Сумма операции','Вид расчета','Место оплаты','Терминал оплаты','Дата оплаты','Время оплаты','Результат операции','Cash-back','Сумма cash-back']
        self.df_dedupped2 = self.df.drop_duplicates(subset=key)
        
        
file_name = "var7.csv"
