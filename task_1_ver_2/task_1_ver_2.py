import pandas as pd # Использую pandas для создания таблицы и перевода времени

# Файл
filename = "2025-10-03.1759515715.074510429.t4433"

list_of_aircrafts = []

try:
    # Открываем файл
    with open(filename, 'r') as file:

        # Читаем строки из файла
        for line in file:

            parts = line.split()

            # Время
            time = float(parts[0])

            # Остальная часть
            string = "".join(parts[1:])
            message = bytearray.fromhex(string)

            # Находим ICAO
            icao = (message[1] << 16) | (message[2] << 8) | (message[3]) # Соединяем остальные

            # Проверяем словарь на наличие записей о борте
            list_of_aircrafts.append({
                'icao': f"{icao:06X}",
                'time': time
            })

    # Переделываем список в DataFrame
    df = pd.DataFrame(list_of_aircrafts)

    # Группируем записи по ICAO и находим первое и последнее время
    summary = df.groupby('icao')['time'].agg(['min', 'max'])

    # Исправляем индекс icao обратно в столбец
    summary = summary.reset_index()

    # Преобразовываем время из Unix формата
    summary['min'] = pd.to_datetime(summary['min'], unit='s')
    summary['max'] = pd.to_datetime(summary['max'], unit='s')

    summary.rename(columns={'icao': 'ICAO адрес','min': 'Первое появление (UTC)', 'max': 'Последнее появление (UTC)'}, inplace=True)

    print(summary)
            

except FileNotFoundError:
    print(f"Файл {filename} не найден!")