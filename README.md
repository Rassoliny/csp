# csp
Система инвентаризации программного обеспечения


<h4>Установка</h4>
git clone https://github.com/Rassoliny/csp

В папке с проектом 
pip install -r requirements

Иногда зависимости сразу не устанавливаются - эта проблема будет решена созданием полноценного инсталлятора

Для демонстрации работы проекта достаточно запустить сервер и клиент на одном и том же хосте на ОС Windows

<h5>Запуск сервера</h5>
python csp/server/corpsoftportal/manage.py runserver 

<h5>Для сбора данных с клиента:</h5>
python csp/Corporate-Software-Client-master/CorporateSoftwareClient.py

<h5>Изменение сервера</h5>
Для того, чтобы использовать не локальный сервер требуется изменить настройки в файле </br>
csp/Corporate-Software-Client-master/CorporateSoftwareClient.py
<ul>
<li>PROTOCOL = 'http'</li>
<li>IP = '127.0.0.1'</li>
<li>PORT = '8000'</li>
<li>URL = 'reciever'</li>
</ul>


<h5>Антентификация через AD</h5>
Проект поддерживает аутентификацию через AD последством django-python3-ldap
Для ее настройки требуется расскоментировать настройки django-python3-ldap в csp/server/corpsoftportal/corpsoftportal/settings.py
