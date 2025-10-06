# Файл
filename = "2025-10-03.1759515715.074510429.t4433"

try:
    # Открываем файл
    with open(filename, 'r') as file:

        # Читаем строки из файла
        for line in file:

            original_line = line.strip() 

            parts = original_line.split()

            # Время
            time_parts = parts[0].split('.') # Разбиваем время на секунды и наносекунды

            seconds = int(time_parts[0]) # Секунд прошло с 1970 года
            nanoseconds = int(time_parts[1]) # Наносекунд прошло с последней секунды

            # Остальная часть
            string = "".join(parts[1:])
            message = bytearray.fromhex(string)

            # Находим DF и ICAO
            df = message[0] >> 3 # Берём первые пять битов от первого байта для DF
            icao = (message[1] << 16) | (message[2] << 8) | (message[3]) # Соединяем остальные

            # Выводим полученное время, DF, ICAO, а также оригинальную строку из файла
            print(f"{original_line} | {seconds}.{nanoseconds} DF: {df} ICAO: {icao}")

except FileNotFoundError:
    print(f"Файл {filename} не найден!")