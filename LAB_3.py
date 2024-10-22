import string
import random

all_symbols = string.ascii_letters + string.digits

# генератор ключа
def generate_key():
    if len(hex_value) != 5:
        print ("Введите пятизначное число!")
        return 0

    dec_value = str(int(hex_value, 16))
    first_part = list(dec_value[:3])
    finish_part = dec_value[-2:]
    

    key = ''
    for i in range (3):
        sequence = random.choices(all_symbols, k=4)
        sequence.insert(random.randint(0,4), first_part[i])
        key += ''.join(sequence)
        if i == 2:
            key += f' {finish_part}'
            break
        key+='-'
    print(key)




    


    


hex_value = input("Введите 5-значное HEX - число: ")
generate_key()



# # Функция для генерации случайного блока символов
# def generate_random_block(length, fixed_char=None):
#     chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     block = ''.join(random.choice(chars) for _ in range(length))
#     if fixed_char is not None:
#         idx = random.randint(0, length - 1)
#         block = block[:idx] + fixed_char + block[idx + 1:]
#     return block

# # Функция для конвертации HEX в ключ
# def convert_hex_to_key():
#     hex_value = hex_input.get().strip()

#     try:
#         # Конвертация из HEX в DEC
#         dec_value = int(hex_value, 16)
#         dec_str = str(dec_value).zfill(6)  # Заполняем нулями до 6 цифр

#         # Генерация случайных блоков с подставлением цифр из DEC
#         block1 = generate_random_block(5, dec_str[0])  # 1-я цифра в 1-й блок
#         block2 = generate_random_block(5, dec_str[1])  # 2-я цифра во 2-й блок
#         block3 = generate_random_block(5, dec_str[2])  # 3-я цифра в 3-й блок
#         last_two = dec_str[3:]  # Последние две цифры

#         # Формирование ключа
#         key = f"{block1}-{block2}-{block3} {last_two}"

#         # Отображение ключа
#         result_label.config(text=f"Ваш ключ: {key}")
#     except ValueError:
#         messagebox.showerror("Ошибка", "Неверное HEX значение. Попробуйте еще раз.")

# # Инициализация окна
# root = tk.Tk()
# root.title("Hex to Dec Key Converter")
# root.geometry("600x400")
# root.resizable(False, False)  # Запрет на изменение размеров окна

# # Инициализация Pygame для воспроизведения музыки
# pygame.mixer.init()
# pygame.mixer.music.load("/Users/tss/Documents/PYTHON LABS/LAB_3/Lab-3/26. Cloudy Park (Sky Area).mp3")
# pygame.mixer.music.play(-1)

# # Загружаем фоновое изображение
# bg_image = Image.open("/Users/tss/Documents/PYTHON LABS/LAB_3/Lab-3/hd-best-kirby-cover-05ijgudtqkv4nagx.jpg")
# bg_image = bg_image.resize((600, 400), Image.LANCZOS)
# bg_photo = ImageTk.PhotoImage(bg_image)

# # Создаем холст для отображения изображения
# canvas = tk.Canvas(root, width=600, height=400)
# canvas.pack(fill=tk.BOTH, expand=True)
# canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

# # Внутренний фрейм для центровки элементов
# frame = tk.Frame(root, bg="black")
# frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# # Поле ввода для HEX значения с "прозрачным" фоном
# hex_input = tk.Entry(frame, font=("Arial", 16), justify='center', bd=0, bg="#d9d9d9", highlightthickness=0)
# hex_input.insert(0, "Введите 5-значное HEX число")
# hex_input.grid(row=0, column=0, pady=20)

# # Кнопка для конвертации с "прозрачным" фоном
# convert_button = tk.Button(frame, text="OK", font=("Arial", 14), command=convert_hex_to_key, bd=0, bg="#d9d9d9", highlightthickness=0)
# convert_button.grid(row=1, column=0, pady=10)

# # Метка для отображения результата с "прозрачным" фоном
# result_label = tk.Label(frame, font=("Arial", 16), fg="white", bg="black")
# result_label.grid(row=2, column=0, pady=20)

# # Запуск приложения
# root.mainloop()

