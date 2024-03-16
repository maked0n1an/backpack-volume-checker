<h1 align="center">Backpack Volume Checker<h1>

The README in Russian can be found here: [README.md](https://github.com/maked0n1an/backpack-volume-checker/blob/main/README.md).

## 🔗 Ссылки
🔔 Channel: 
[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/crypto_maked0n1an)](https://t.me/crypto_maked0n1an)

<h2>Описание</h2>
Бот создан для проверки объема в BackPack. Код выполняется асинхронно, данные не часто совпадают с сайтом

Для работы нужно вставить:
- куки в 'input_data/cookies'; 
- прокси в 'input_data/proxies.txt'; 
- имена для аккаунтов в 'input_data/account_names.txt' (опционально, читай 'input_data/config.py')
Форк от автора: https://github.com/3asyPe/backpack-volume-checker

Как получить куки?
1. Залогиньтесь на каждый аккаунт проекта;
2. Нажмите F12;
3. Зайдите на вкладку «Сеть» любой файл, который будет .
3. Нажмите фильтр 'Fetch/XHR' чуть ниже;
4. Берем любой файл, который будет с оранжевым знаком и без расширения (например, файл 'user' или 'capital' или 'assets').
5. В Request Headers найдите header/секцию под названием 'Cookie' и полностью скопируйте её значение
6. Вставьте в 'input_data/cookies', одни куки - одна строка

Подробнее на скрине ниже:
![](https://github.com/maked0n1an/backpack-volume-checker/blob/main/instruction.png)


## Установка и запуск
Если у тебя нет знаний по поводу установки Питона и его запуска, аудита софтов, то тебе в раздел [Ccылки](#ссылки):

* Устанавливаем библиотеки:
<pre><code>pip install -r requirements.txt</code></pre>
* Заходим в папку zk-bridge:
<pre><code>cd backpack-volume-checker</code></pre>
* Прочти 'input_data/settings.py' внимательно и сделай настройку.
* Запускаем в терминале:
<pre><code>python main.py</code></pre>

## Донаты (EVM): 
<pre><code>0x74eEfCAD1Ad18705596106703A3036BaAD6B3145</code></pre>

## Отказ от ответственности и рекомендации по Безопасности

Любое использование данного продукта осуществляется на усмотрение конечного пользователя. В контексте данного использования включаются, но не ограничиваются, сферы потери девственности, финансовых средств и суеверных практик.
Отмечаем, что за потерянные денежные средства, произошедшие в результате использования продукта, мы не несем ответственности. Рекомендуем внимательно ознакомиться с кодом продукта, произвести его полный осмотр, и удостовериться в том, что данные не передаются или не "утекают" в процессе его функционирования.

## Ссылки 
<a name="Ссылки"></a> 
- https://t.me/crypto_maked0n1an
- [Гайд по аудиту софтов на наличие скамов](https://teletype.in/@brokeboi/dsxymHafdZb)
- [Ультимативный гайд по запуску скриптов. Python.](https://teletype.in/@hodlmod.eth/how-to-run-scripts)
