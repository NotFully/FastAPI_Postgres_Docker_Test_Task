import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .main import app, get_db

DATABASE_URL = "postgresql://postgres:123qwe@localhost/postgres"

# Настройка тестовой базы данных
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Функция для создания тестовой базы данных
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Инициализация тестового клиента
client = TestClient(app)


# Фикстура для установки и очистки тестовой базы данных
@pytest.fixture(scope="function")
def test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


# Тест для создания элемента
def test_create_item(test_db):
    item_data = {"name": "Test Item", "price": 10.0, "photo": "test.jpg"}
    response = client.post("/api/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == item_data["name"]
    assert response.json()["price"] == item_data["price"]
    assert response.json()["photo"] == item_data["photo"]


# Тест для обновления элемента
def test_update_item(test_db):
    # Создаем элемент для обновления
    create_response = client.post("/api/items/", json={"name": "Update Test", "price": 10.0, "photo": "test.jpg"})
    assert create_response.status_code == 200
    created_item = create_response.json()

    # Обновляем элемент
    update_data = {"name": "Updated Test", "price": 15.0, "photo": "updated_test.jpg"}
    update_response = client.patch(f"/api/items/{created_item['id']}", json=update_data)
    assert update_response.status_code == 200
    updated_item = update_response.json()

    # Проверяем, что элемент успешно обновлен
    assert updated_item["name"] == update_data["name"]
    assert updated_item["price"] == update_data["price"]
    assert updated_item["photo"] == update_data["photo"]
