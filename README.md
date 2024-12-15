## Бизнес-кейс
Система: Платформа для онлайн-торговли. <br>
Основные задачи платформы:
- управление пользователями,
- обработку заказов,

## Выделение микросервисов
Для реализации симитированы два микросервиса:

- UserService: управление пользователями (регистрация, аутентификация).
- OrderService: обработка заказов (создание заказа, получение информации о заказе)

## Предварительные шаги для настройки окружения
### Установка зависимостей на ОС Ubuntu
1. Обновление системы: <br>
`sudo apt update && sudo apt upgrade -y`

2. Установка Python и pip: <br>
`sudo apt install python3 python3-pip -y`

3. Установка виртуального окружения: <br>
`sudo pip3 install virtualenv`

4. Установка gRPC и других инструментов: <br>
`sudo apt install protobuf-compiler -y` <br>
`pip3 install grpcio grpcio-tools`

5. Создание и активация виртуального окружения: <br>
`python3 -m venv grpc_env` <br>
`source grpc_env/bin/activate`

6. Установить Docker <br>
   [Документация по установке на Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## Запуск проекта
`docker-compose up --build`
