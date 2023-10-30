![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

# My-routes - это мини-утилита для отображения маршрутов на карте. 

Многие приложения позволяют видеть информацию и карту отдельного маршрута. Эта же утилита поможет отобразить сразу все выбранные Вами маршруты на одной карте и посчитать общую дистанцию.

### Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Aleksentcev/my-routes.git
```

```
cd my-routes
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Скопировать Ваши файлы .gpx в папку data (Практически любой сервис для отслеживания тренировок позволяет получить данные об активностях в таком формате):

```
my-routes/data/
```

Запустить проект:

```
python3 app_runner.py
```

Дождаться пока карта со всеми маршрутами будет сгенерирована.

Проект будет доступен по адресу: http://127.0.0.1:5000/. Если ничего не заработало - идите пить чай :)

### Автор:

Михаил Алексенцев

[![Telegram](https://img.shields.io/badge/aleksentcev-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&link=https://t.me/aleksentcev)](https://t.me/aleksentcev)
