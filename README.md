# PlantAI_API


This is a Django-based API that provides machine learning capabilities for PlantAI. It allows you to to identify and diagnose plants.

## License

The Django Machine Learning API project is licensed under the MIT License. For more details, please see the [LICENSE](LICENSE) file.

## Installation

Follow these steps to install and set up the Django Machine Learning API ():

1. Clone the repository:
    ```bash
    git clone https://github.com/Aeidle/PlantAI_API.git
    ```


2. Change into the project directory:
    ```bash
    cd PlantAI_API
    ```

3. Create and activate a virtual environment
    ```bash
    python -m venv venv
    [comment]: <> (This is a comment, it will not be included)
    source venv/bin/activate <!-- for macOS/Linux --> 
    [//]: <> (This is also a comment.)
    venv\Scripts\activate <!-- for Windows -->
    [//]: # (This may be the most platform independent comment)
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Perform database migrations:
    ```bash
    python manage.py migrate
    <!-- If the above command did not work, you can try running the following two commands instead: -->
    python manage.py makemigrations
    python manage.py migrate
    ```



## Usage

Follow these steps to run the Django Machine Learning API:

1. Make sure your virtual environment is activated (if you created one).

2. Start the development server:
    ```bash
    python manage.py runserver
    ```

3. The API will now be accessible locally at `http://localhost:8000/`. Use a tool like [Postman](https://www.postman.com/) to send requests to the API endpoints.

- **Endpoint**: `/file/upload/`
- **Method**: `POST`
- **URL**: `http://localhost:8000/file/upload/`
- **Request Format**:
  - The API expects an RGB image (squared for best results).
  - The following fields should be provided:
    - `key: remark`, `value: anything`
    - `key: type`, `value: fruit or leaf`
    - `name: if fruit, write 'none'. If leaf, write the name of the plant with the first letter in uppercase and in singular form (e.g., Potato). If the name is composed, write both first letters in uppercase separated by an underscore (e.g., Bell_Pepper)`.
- **Response Format**:
  - The API will return a JSON response containing the 3 best results.
  - Each result will have the following keys:
    - `key: name`, `value: plant_name`
    - `key: condition`, `value: healthy or disease name`
    - `key: type`, `value: fruit or leaf`

## Contributing

Contributions are welcome! If you'd like to contribute to the Django Machine Learning API project, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name:
    ```git
    git checkout -b <branch_name>
    ```

3. Make your desired changes to the codebase.

4. Commit your changes:
    ```git
    git commit -m "<commit_message>"
    ```

5. Push the changes to your forked repository:
    ```git
    git push origin <branch_name>
    ```

6. Open a pull request on the original repository and describe your changes.

