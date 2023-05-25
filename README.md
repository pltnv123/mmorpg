# Доска объявлений для фанатского MMORPG-сервера

Техническое задание:

"Нам необходимо разработать интернет-ресурс для фанатского сервера одной известной MMORPG — что-то вроде доски объявлений. Пользователи нашего ресурса должны иметь возможность зарегистрироваться в нём по e-mail, получив письмо с кодом подтверждения регистрации. После регистрации им становится доступно создание и редактирование объявлений. Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент. Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста. При отправке отклика пользователь должен получить e-mail с оповещением о нём. Также пользователю должна быть доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также должно прийти уведомление). Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Также мы бы хотели иметь возможность отправлять пользователям новостные рассылки."

---
Запуск проекта:
Т.к. данный проект разрабатывался на ОС Windows 11, все нижеуказанные команды приведены для запуска проекта на такой же ОС.

1. Клонируем проект из удалённого репозитория на GitHub:

   - git clone https://github.com/pltnv123/mmorpg.git

2. Устанавливаем необходимые для работы проекта зависимости:

    - pip install -r requirements.txt

3. Активируем виртуальное окружение:

   - venv\scripts\activate

4. Открываем 2 дополнительных окна терминала (т.е. всего их должно быть три) и в каждом из них переходим в директорию проекта:

    - cd mmorpg

5. в первом окне терминала запускаем Celery для асинхронной обработки задач по отправке писем (все письма должны приходить в текстовом формате именно в это окно терминала):

    - celery -A mmorpg worker -l INFO --pool=solo
6. во втором запускаем обработку периодических задач через Celery (очистка неподтверждённых аккаунтов пользователей и удаление неиспользованных кодов авторизации из БД):

    - celery -A mmorpg beat -l INFO

7. в последнем окне терминала запускаем наш Django-сервер:

   - py manage.py runserver

8. переходим по ссылке:

  - http://127.0.0.1:8000/


