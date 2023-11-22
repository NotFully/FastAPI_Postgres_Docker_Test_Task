# FastAPI Test Task

## Запуск проекта с использованием Docker

1. Установите Docker и Docker Compose, если они не установлены.
2. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/NotFully/FastAPI_Postgres_Docker_Test_Task/
   ```

3. Перейдите в каталог проекта.
4. Создайте файл '.env' в корневом каталоге проекта и укажите переменные окружения для подключения к базе данных PostgreSQL:
   
   ```bash
   POSTGRES_USER=<your_user>
   POSTGRES_PASSWORD=<your_password>
   POSTGRES_SERVER=<your_server>
   POSTGRES_PORT=5432
   POSTGRES_DB=<your_db_name>
   ```
6. Запустите приложение с помощью Docker Compose:
   
   ```bash
   docker-compose up --build
   ```

## Работа с API

API предоставляет следующие эндпоинты:

1. POST ```http://localhost:8000/api/items/```: Создание нового элемента.
2. PATCH ```http://localhost:8000/api/items/{item_id}```: Обновление существующего элемента.
3. DELETE ```http://localhost:8000/api/items/{item_id}```: Удаление элемента.
4. GET ```http://localhost:8000/api/buyers/```: Получение списка покупателей.
5. GET ```http://localhost:8000/api/items/```: Получение списка элементов.
6. GET ```http://localhost:8000/api/items/{item_id}/buyers/```: Получение списка покупателей для конкретного элемента.
7. GET ```http://localhost:8000/api/buyers/{buyer_id}/items/```: Получение списка элементов для конкретного покупателя.
8. Документация API доступна по адресу ```http://localhost:8000/docs```.
