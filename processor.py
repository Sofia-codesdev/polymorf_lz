import pandas as pd

class DataProcessor:
    def __init__(self, filepath):
        try:
            self.df = pd.read_csv(filepath, encoding='utf-8-sig')
            print(f"Данные успешно загружены. Всего строк: {len(self.df)}")
        except FileNotFoundError:
            print(f"Файл {filepath} не найден.")
            self.df = pd.DataFrame()

    def split_and_save(self):
       
        if self.df.empty:
            return

        # Разделение на физ. и юр. лица
        self.df_phys = self.df[self.df['Участники гражданского оборота'] == 'физ. лицо'].copy()
        self.df_legal = self.df[self.df['Участники гражданского оборота'] == 'юр. лицо'].copy()

        # Сохранение в отдельные файлы
        self.df_phys.to_csv('phys_persons.csv', index=False, encoding='utf-8-sig')
        self.df_legal.to_csv('legal_entities.csv', index=False, encoding='utf-8-sig')
        
        print("Файлы успешно сохранены: 'phys_persons.csv' и 'legal_entities.csv'")

    def __invert__(self):
       
        if self.df.empty:
            return 0
        
        initial_count = len(self.df)
        # Удаляем дубликаты
        self.df.drop_duplicates(inplace=True)
        final_count = len(self.df)
        
        deleted_count = initial_count - final_count
        
        # Опционально: обновляем сохраненные файлы после очистки
        self.split_and_save()
        
        return deleted_count