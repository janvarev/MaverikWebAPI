# Maverik WEB api

Небольшой Python-сервер на FastAPI, позволяющий
с помощью HTTP-вызовов переводить кусок экрана с помощью
[Maverik OCR Helper](https://maverikocrhelper.blogspot.com/)

#### Как работает
- запустите файл
- будет запущен сервер на порту 5001
- обычно доки можно посмотреть на http://127.0.0.1:5001/docs
- вызовите функцию translate, параметры
  - x,y - координаты левой верхней точки экрана для распознавания
  - x2,y2 - правой нижней
  - copyTrans - 0 если сразу получить содержимое буфера обмена,
  1 - если попытаться скопировать перевод 
  (важно: окно Маверик должно быть для этого видимо и располагаться в верхнем левом углу)

Функция работает через эмуляцию клавиш и мыши (pyautogui)

#### Сборка через auto-py-to-exe

Для работы в сторонней программе имеет смысл собрать 
для этого сервера EXE-файл со всем нужным (вместо питона)

Сборка отлично работает; только нужно указать скрытый импорт основного модуля
```
--hidden-import "runtranslationserver"
```

#### Готовый EXE

Скачать готовый EXE можно здесь:

[v1.0](https://download.janvarev.ru/maverikwebapi/runtranslationserver10.exe)
