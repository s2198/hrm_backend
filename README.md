## 시작 가이드

### 요구사항
* Python 3.11
* manage

3. DB 마이그레이션 및 서버 시작
```
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py createcustomgroup
python manage.py createptotype
python manage.py runserver
```
