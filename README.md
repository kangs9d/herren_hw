<h1>herren HW</h1>

POSTMAN에서 collection으로 만들어져있습니다.<br>
DB는 간단하게 SQLite를 이용했고, sendEmail에서 multiProcessing을 이용했습니다.
<h6>확인 URL:</h6> 
https://www.getpostman.com/collections/a598e9add06e6c29680f


<h3><b>curl로 확인</b></h3>

1. subscribe API : POST subscribe

curl --location --request POST 'localhost:8000/api/v1/subscribe' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=<my_username>' \
--data-urlencode 'email=<my_email>'

2. unsubscribe API : POST subscribe

curl --location --request POST 'localhost:8000/api/v1/unsubscribe' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'email=<my_email>'

3. sendEmail API : POST send_email

curl --location --request POST 'localhost:8000/api/v1/mail' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'subject=<my_subject>' \
--data-urlencode 'content=<my_content>'



