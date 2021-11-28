# photo_uploader

Функционал:
Загрузка изображений (доступно авторизованному пользователю при наличии аутентификации).

Сценарий работы API:
Метод API принимает одно или несколько изображений и сохраняет их в папку. Для передачи используется POST запрос с содержимым multipart/form-приложений. Для отправки multipart/form-приложений используется REST Client.

Дополнительный функционал:
Валидация загружаемых изображений — максимальный размер 200кб.
Изображение сохраняется с уникальным названием - уже встроено в Django.

### Запуск
- git clone https://github.com/Hawool/photo_uploader.git
- cd photo_uploader
- docker-compose up -d --build
- docker-compose exec api python manage.py migrate --noinput

### Есть всего два метода для изображений: get, post
#### Загрузка изображения:  
```
curl --location --request POST 'http://localhost:8000/api/v1/photos'  
--header 'Authorization: Token %userToken'  
--form 'owner=%owner_id'  
--form 'image=%image'  
```
или  
```
--header 'Authorization: Token %userToken'  
--form 'image_1=%image_1'  
--form 'image_2=%image_2'  
--form 'image_3=%image_3'  
```

#### Получение всех изображений:
```
curl --location --request GET 'http://localhost:8000/api/v1/photos'  
--header 'Authorization: Token %userToken'  
```

#### Регистрация пользователя:
```
curl --location --request POST 'http://localhost:8000/auth/users/'  
--form 'username=%username'  
--form 'password=%password'  
```  
#### Получение токена авторизации пользователя:
```
curl --location --request POST 'http://localhost:8000/auth/token/login/'  
--form 'username=%username'  
--form 'password=%password'  
```

