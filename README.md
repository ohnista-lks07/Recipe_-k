# 🍳 Recipe Book

> Особиста кулінарна книга — зберігай рецепти, діліться з іншими, надихайся новими стравами.

![Python](https://img.shields.io/badge/Python-3.13-green?style=flat-square)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat-square)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-green?style=flat-square)

---

## ✨ Можливості

- 📖 Перегляд публічних рецептів від усіх користувачів
- 👤 Особистий кабінет з власними рецептами
- ➕ Додавання рецептів з фото, інгредієнтами та способом приготування
- ✏️ Редагування та видалення власних рецептів
- 💬 Відгуки до рецептів
- 🔒 Приватні та публічні рецепти
- 🔐 Реєстрація та авторизація

---

## 🛠 Технології

- **Backend:** Python, Django
- **Frontend:** Bootstrap 5, HTML, CSS
- **База даних:** SQLite
- **Авторизація:** Django Auth

---

## 🚀 Запуск проекту

### 1. Клонуй репозиторій
```bash
git clone https://github.com/ohnista-lks07/Recipe_-k.git
cd Recipe_-k
```

### 2. Створи віртуальне середовище
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Встанови залежності
```bash
pip install -r requirements.txt
```

### 4. Налаштуй змінні середовища
```bash
cp .env.example .env
```
Відкрий `.env` і заповни:
SECRET_KEY=твій-секретний-ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
### 5. Зроби міграції
```bash
python manage.py migrate
```

### 6. Створи суперюзера
```bash
python manage.py createsuperuser
```

### 7. Запусти сервер
```bash
python manage.py runserver
```

Відкрий браузер: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Структура проекту
```
RecipeBook/
├── Recipe/              # Основний застосунок
│   ├── models.py        # Моделі: Recipe, Category, Ingredient, Review
│   ├── views.py         # Логіка сторінок
│   ├── forms.py         # Форми
│   ├── urls.py          # URL маршрути
│   └── admin.py         # Адмін панель
├── config/              # Налаштування проекту
│   ├── settings.py
│   └── urls.py
├── templates/           # HTML шаблони
│   ├── base.html
│   ├── Recipe/
│   └── registration/
├── .env.example         # Шаблон змінних середовища
├── .gitignore
├── manage.py
└── requirements.txt
---
```

## 📊 Моделі бази даних
```
| Модель | Поля |
|--------|------|
| `Category` | name |
| `Recipe` | title, author, category, image, text_content, is_public, created_at |
| `Ingredient` | recipe, name, amount, unit |
| `Review` | recipe, author, message, created_at |
```
---

## 👩‍💻 Автор 
GitHub: [@ohnista-lks07](https://github.com/ohnista-lks07)
