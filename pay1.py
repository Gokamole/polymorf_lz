import os
import pandas as pd
df = pd.read_csv("var7.csv")
key = ['Участники гражданского оборота','Тип операции','Сумма операции','Вид расчета','Место оплаты','Терминал оплаты','Дата оплаты','Время оплаты','Результат операции','Cash-back','Сумма cash-back']
df_dedupped2 = df.drop_duplicates(subset=key)
print(df.shape)
print(df_dedupped2.shape)