# Backend
### Virtual Enviroment:
1. create new python enviroment in the root of this repo
```python3 -m venv env```

2. Activate this enviroment
```source env/bin/activate```

3. Install or uptade the python's packages
```pip install -r backend/requirements.txt```

4. Run kibana and elasticsearch (instructions in backend/database/elastic/README.md)

<br>

### API Executions:
* **Running Django API**:
    Move to _backend/api_ folder and execute:
    ```sh
    python3 manage.py runserver
    ```
* **Using Backend Linter:**
    * Set packages to be analysed or ignored on file _backend/api/env.py_
    * Executing linter:
        * Go to folder _backend/api/linter_
        * Execute:
            ```sh
            python3 lint_script.py
            ```
        * Output is on a file on the same folder called **log_linter.txt**
