В проекте реализованы 3 теста на добавление, изменение и поиск объявлений:
1) Добавление нового объявления реализовано в test_add.py
   В данном файле перед описанием функции указаны параметры (название, цена, описание и ссылка на изображение), которые будут использованы при тестировании.
   
2) Изменение готового объявления реализовано в test_edit.py
   В данном файле перед описанием функции указаны параметры (старое название, новое название, старая цена, новая цена, описание и ссылка на изображение), которые будут использованы при тестировании.

3) Поиск объявления реализовано в test_search.py
   Перед функцией необходимо перечислить слова, которые будут использованы при тестировании поиска

Для запуска необходимо загрузить файлы и запустить тестирование через консоль с помощью комманды pytest
Данные тесты также были запущены с помощью Github Actions
