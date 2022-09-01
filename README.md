# Парсер бесплатных прогнозов на футбол с сайта https://vprognoze.ru/robobet/

Парсер разработан для сохранения всех результатов прогнозов для дальнейшей статистической валидации работы исскусственного интелекта. 

## Установка
### 1) Необходимо клонировать проект на локальную машину:

```bash
git clone https://github.com/RomanLazovskiy/Robobet_Parser.git
```

### 2) Установить Docker

#### Для OSX/Linux/bashonwindows
https://docs.docker.com/desktop/install/windows-install/

#### Для OSX/Linux/bashonwindows
https://docs.docker.com/desktop/install/linux-install/
(Все интрукции можно найти в интернете)

### 3) Утановить Docker-compose
https://docs.docker.com/compose/install/
(Все интрукции можно найти в интернете)

## Изменение конфигурации

### 1) Изменить настройки в файле docker-compose.yaml
Необходимо указать имя пользователя и пароль которое будет использовано при создании базы данных.
```
- POSTGRES_USER=
- POSTGRES_PASSWORD=
```

### 2) Изменить настройки в файле config.py
Необходимо указать имя пользователя и пароль для входа в базу данных, такие же какие-прописаны в файле docker-compose.yaml
```
'user': '',
'password': '',
```

## Запуск Docker контейнеров
Для запуска контейнеров необходимо открыть командную строку и перейти в папку с проектом. 
Далее запустите docker-compose.yaml командой:

```bash
sudo docker-compose up -d
```

Проверить запуск контейнеров можно командой: 

```bash
sudo docker ps
```
Или посмотреть log работы docker-compose:
```bash
sudo docker-compose logs
```
Для того чтобы зайти в базу данных можно использовать команду:
```bash
psql -U user(котороый указывали при создании бд) -d robobet -h 127.0.0.1 -W
```

## Структура таблицы в бд

```
id - id матча
event_start_time - время начала матча
event_league - лига в которой играется матч
team_1_name - имя первой команды
team_2_name - имя второй команды
first_team_percentage - прогнозируемый процент победы первой команды
draw_percentage - прогнозируемый процент ничьи
second_team_percentage - прогнозируемый процент победы второй команды
event_forecast - ставка ии
first_team_odd - коэффициент букмекера на победу первой команды
draw_odd  - коэффициент букмекера ничья
second_team_odd - кофициент букмекера на победу второй команды
event_result - результат матча
```
