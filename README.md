# PlantAI_API


This is a Django-based API that provides machine learning capabilities for PlantAI. It allows you to to identify and diagnose plants.

## License

The Django Machine Learning API project is licensed under the MIT License. For more details, please see the [LICENSE](LICENSE) file.

## Installation

Follow these steps to install and set up the Django Machine Learning API:

1. Clone the repository:

```git clone https://github.com/Aeidle/PlantAI_API.git```


2. Change into the project directory:

```cd PlantAI_API```


3. Create and activate a virtual environment

```python -m venv venv```
```source venv/bin/activate # for macOS/Linux```
```venv\Scripts\activate # for Windows```


4. Install the required dependencies:

```pip install -r requirements.txt```


5. Perform database migrations:

```python manage.py migrate```
<!-- if it did not work use this two commands instead -->
```python manage.py makemigrations```
```python manage.py migrate```


## Usage

Follow these steps to run the Django Machine Learning API:

1. Make sure your virtual environment is activated (if you created one).

2. Start the development server:

```python manage.py runserver```


3. The API will now be accessible locally at `http://localhost:8000/`. You can use a tool like [Postman](https://www.postman.com/) to interact with the API endpoints.

4. [Provide instructions or examples on how to use the API, including the available endpoints, request/response formats, and any authentication/authorization requirements.]

## Contributing

Contributions are welcome! If you'd like to contribute to the Django Machine Learning API project, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name:

```git checkout -b <branch_name>```

3. Make your desired changes to the codebase.

4. Commit your changes:

```git commit -m "<commit_message>"```

5. Push the changes to your forked repository:

```git push origin <branch_name>```


6. Open a pull request on the original repository and describe your changes.



