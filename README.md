# ДЗ: первый мини-проект [![Build Status](https://travis-ci.org/pahaz/homework-simple-python-web-application.svg?branch=master)](https://travis-ci.org/pahaz/homework-simple-python-web-application) #

Предлагается сделать один из следующих мини-проектов:

 1. [сервис "плохой-сайт.ру"](#1-%D0%BF%D0%BB%D0%BE%D1%85%D0%BE%D0%B9-%D1%81%D0%B0%D0%B9%D1%82%D1%80%D1%83)
 2. [сервис "слил-файл.ру"](#2-%D1%81%D0%BB%D0%B8%D0%BB-%D1%84%D0%B0%D0%B9%D0%BB%D1%80%D1%83)
 3. [сервис "сократи-ссылку.ру"](#3-%D1%81%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%B8-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83%D1%80%D1%83)
 4. [сервис "расшарь-код.ру"](#4-%D1%80%D0%B0%D1%81%D1%88%D0%B0%D1%80%D1%8C-%D0%BA%D0%BE%D0%B4%D1%80%D1%83)

### 1. "плохой-сайт.ру" ###
**книга жалоб интернета** или **www.huzhe.net**
 - возможность оставить жалобу на какой-то ресурс
 - возможность редактирования своей жалобы
 - возможность удаления свой жалобы

### 2. "слил-файл.ру" ###
**файлообменник для студентов** или **ge.tt** или **anonfiles.com**
 - возможность заливать/скачивать файлы
 - возможность посмотреть количество скачиваний
 - возможность удалить свой файл
 - режим "удалить файл после первого скачивания"

### 3. "сократи-ссылку.ру" ###
**твиттер символо-экономилка** или **bitly.com**
 - возможность сокращения ссылки
 - возможность посмотреть количество переходов по ссылке
 - возможность удалить свою ссылку
 - режим "удалить ссылку после первого перехода"

### 4. "расшарь-код.ру" ###
**кода-копипаста** или **pastebin.com**
 - возможность вставки/просмотра кода с сохранением форматирования
 - подсветка синтаксиса (http://pygments.org/)
 - возможность удалить свой код
 - режим "удалить код после первого просмотра"

### Интересные идеи микро-проектов: ###
 - online base64, base32, base16, MD5, AES, SHA-1, ...
 - online unzip, unrar, untar, ungz, ...
 - online text diff
 - online encoding detector (ru)
 - online python, ruby, node.js, php, ...
 - online compile, C#, C++, ANSI C, ...
 - online port scan

# Требования #

Для задачи использовать любой из рассмотренных фреймворков: 

 - http://bottlepy.org/docs/dev/index.html
 - http://werkzeug.pocoo.org/
 - http://jinja.pocoo.org/docs/
 - http://flask.pocoo.org/
 - http://www.tornadoweb.org/en/stable/

Требования: 

 - Хранить данные не в памяти.
 - Использовать шаблоны (например Jinja2).
 - Оформить внешний вид (попытаться).
