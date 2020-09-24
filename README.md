# auth-service-testing
Một đoạn code nhỏ để học tập môn Kiểm thử phần mềm.

## Công nghệ sử dụng :
- Ngôn ngữ : Python 3.
- Framework: Flask.
- Thư viện : flask-plus (xây dựng ứng dụng Restfull API), flask-sqlalchemy (khởi tạo, xử lí database), flask-migrate (migrate database), 
flask-bcrypt (mã hóa mật khẩu), flask-testing (viết unit test), pyJWT (quản lí access token).

## Cấu trúc dự án :
- app/main : Implement chức năng.
Luồng xử lí : controller(handler) -> service -> model (repo).
- app/test : Unit test cho các chức năng.

## Cách cài đặt :
- Clone repo to local.
```
git clone https://github.com/nhatminhk63j/auth-service-testing/
```
- Install system package :
```
sudo apt install python-pip -y
```
- Install python package :
```
pip install -r requirements.txt
```
- Active venv:
```
source venv/bin/activate
```
- Run:
```
python3 manage.py run
```
- Test:
```
python3 manage.py test
```