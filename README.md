# Note
Приложение на Python для вывода заметки, которая всегда перед глазами.

## Проблема
Не хватало лаконичного решения для размещения важной текстовой информации.

## Требования
1. Поверх всех окон.
2. Стилистически без нагромождений - прозрачный фон.
3. Минимальный набор функций.
4. Данные по настройкам и содержимому хранятся в двух файлах рядом с исполняемой программой в settings.txt и text.txt.
5. Заметку можно перемещать.

## Решение
Скрипт на Python с использованием библиотеки PyQt5 + использование pyinstaller для компиляции в EXE-файл.

## Установка
Получение репозитария.
```
git clone <note.git>
```
Установка на Windows.
```
pip install pyinstaller
pyinstaller --onefile --noconsole --clean --icon=note.ico note.py
```
После компиляции появятся две дополнительные папки и файл с расширением .spec.
```
/note_dir
-- /dist
-- /build
-- .spec
-- note.py
-- note.ico
```
В папке dist будет исполняемый EXE файл. Для удобства можно добавить в автозагрузку.
Папку build и файл с расширением .spec можно удалить.

После запуска приложения создаются два файла в той же директории settings.txt и text.txt.
```
/note_dir
-- /dist
---- note.exe
---- settings.txt -> настройки приложения (местоположение, размер окна)
---- text.txt -> содержимое заметки
-- note.py
-- note.ico
```


## Скриншоты
Общий вид.
<img width="1116" height="551" alt="image" src="https://github.com/user-attachments/assets/a98c1dad-4746-4a7d-9980-22f081fa8bbe" />

Меню.
<img width="1069" height="496" alt="image" src="https://github.com/user-attachments/assets/f14e3921-a379-422b-b3f1-7439e1095403" />

Редактирование.
<img width="1146" height="640" alt="image" src="https://github.com/user-attachments/assets/b8b49382-c2d4-4260-973b-35efb79110c2" />
