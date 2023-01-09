# Extrahop Challange

### Setup
- The API is built using Django Rest Framework (DRF)
- Make sure you have python 3.8+ installed in your system
- Navigate to the directory containing manage.py
- Create a python virtual environment:
```
python3 -m venv venv
```
- Activate the virtual environment:
```
source venv/bin/activate
```
- Install requirements:
```
pip install -r requirements.txt
```
- Replace file path in constants.py
- Run the server using
```
python manage.py runserver
```
- The server will be live on http://localhost:8000

### Run API
- To get all users
```
GET request on `http://localhost:8000/`
```
- To get user detailts
```
GET request on `http://localhost:8000//user/username`
```
- To delete a user
```
DELETE request on `http://localhost:8000//user/username`
```


