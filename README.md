# AI 자동화 HRM 플랫폼 
안녕하세요. HRM 업무가자동화되지않은스타트업, 중소기업을 위한스마트HRM 플랫폼 만들었습니다. 
최근 빈번해진 인력 이동과 잦은 채용 및 원격 근무로 인하여 가중된 HR 업무의 부담을 줄이고 인재 관리의 효율성을 높이기 위한 스마트 솔루션 제공 선정

# 구동모습
<p align="center">
<img src="https://github.com/user-attachments/assets/e84ab43e-cbe8-49ad-b107-67471a4966d2">
</p>


<br>
<p align="center">
<img src="https://github.com/user-attachments/assets/a52cb6c5-2b6c-4e6a-a123-c105a45ea5a5">
</p>
## 시작 가이드

### 요구사항
* Python 3.11
* manage

1. DB 마이그레이션 및 서버 시작
```
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py createcustomgroup
python manage.py createptotype
python manage.py runserver
```

