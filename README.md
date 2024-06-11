# Task Manager

A simple web application for managing tasks with a RESTful API.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/prudhvikollanapK/bdiplus.git
    cd bdiplus
    ```

2. **Set up the virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Run the application**:
    ```bash
    cd frontend
    python -m http.server 5000 --bind localhost
    ```

7.**Open this url in browser**
  ```bash
http://127.0.0.1:5000
```


## Testing

Run the tests with the following command:

```bash
python manage.py test
```

## UI screens

![image](https://github.com/prudhvikollanapK/bdiplus/assets/86195686/1fc3b28b-bd6d-478c-94ab-4b287ae32322)
![image](https://github.com/prudhvikollanapK/bdiplus/assets/86195686/bfef8e94-0027-4e99-94cb-163343c336ff)
![image](https://github.com/prudhvikollanapK/bdiplus/assets/86195686/d8578bef-67ff-4221-a261-aaa961af1676)

## Database adminstration
![image](https://github.com/prudhvikollanapK/bdiplus/assets/86195686/fcded724-54ae-4e02-8d6c-a2039de9df23)



