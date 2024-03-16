def get_cats_info(path):
    file_path = 'cat.txt'
    cats=[]
    try:
       with open('cat.txt', 'r', encoding= 'utf-8') as file:
           for line in file:
                try:
                    dannye_cats = line.strip().split(',')
                    cat_id = dannye_cats[0]
                    cat_name = dannye_cats[1]
                    cat_age = dannye_cats[2]
                    cat = {'id': cat_id, 'name': cat_name, 'age': int(cat_age)}
                    cats.append(cat)    
                except ValueError:
                    print(f"Помилка у форматі рядка: {line.strip()}")
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")  
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats
      
   
    
cats_info = get_cats_info("cat.txt")
print(cats_info)                    
    
    