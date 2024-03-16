def total_salary(Path):
    total = 0
    count = 0
    file_path = "name.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    money = line.strip().split(',')                    
                    total += int(money[1])                
                    count += 1                  
                except ValueError:
                    print(f"Помилка у форматі рядка: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл '{Path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    if count > 0:
        average_salary = int(total / count)
    else:
        average_salary = 0

    return total, average_salary


total, average = total_salary('file_path')

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


