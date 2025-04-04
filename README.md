# Caesar Cipher

Программа, реализующая шифр Цезаря для сообщений на английском языке.

## Структура проекта
tree /F

C:.
│   .gitignore
│   README.md
│   requirements.txt 
│
└───caesar_cipher
    ├───src
    │       cipher.py
    │       __init__.py
    │
    └───tests
            test_cipher.py
            __init__.py


* requirements.txt - требования (необходимые библиотеки)
* cipher.py - основной код
* test_cipher.py - юнит-тесты

# Запуск проекта:

1. Клонируем репозиторий: 
git clone https://github.com/yourusername/caesar_cipher.git

2. Заходим в папку caesar_cipher:
cd caesar_cipher

3. Устанавливаем зависимости:
pip install -r requirements.txt

4. Для запуска программы:
python src/cipher.py "Your message" 3

5. Запустить тесты:
python -m unittest discover -s tests