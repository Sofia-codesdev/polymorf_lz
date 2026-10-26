from processor import DataProcessor

def main():
    # Путь к файлу 
    filepath = 'var1.csv'
    # Создаем экземпляр класса
    processor = DataProcessor(filepath)
    
    # 1. Разделяем данные и сохраняем в два файла
    processor.split_and_save()
    
    # 2. Используем унарный оператор ~ для удаления дубликатов
    deleted_rows = ~processor
    
    # 3. Выводим результат
    print(f"Количество повторяющихся строк в наборе данных: {deleted_rows}")

if __name__ == "__main__":
    main()