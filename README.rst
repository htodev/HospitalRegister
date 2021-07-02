HospitalRegister
================================================

  HospitalRegister provides functionality for HospitalRegister project.

Meta
-------

Author:
    Hristo Todev

Status:
    Done

Django Version:
    3.1.3

Python Version:
    3.8.1

Usage
--------

How to activate venv and install package requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    > install python 3.8

    > python -m {PATH_TO_VENV_FOLDER}

    > <PATH_TO_VENV_FOLDER>\Scripts\activate

    > pip install -r requirements.txt

    * if there is some problems about installing Pillow, run this script:
    > python -m pip install --upgrade Pillow

    (Windows)


    $ sudo apt-get install python3.8

    $ virtualenv --python=/usr/bin/python3.8 ${PATH_TO_VENV}

    $ source ${PATH_TO_VENV}/bin/activate

    $ pip install -r requirements.txt

    (Linux)


Urls
-----------

::

    hospital_units(public)
        # /hospital_units/
        # /hospital_units/doctors/
        # /hospital_units/myrecords/ (authenticated)

    Authentication
        # /auth/register/
        # /auth/login/
        # /auth/profile/
        # /auth/profile/edit/

    Enrollment(authenticated)
        # /enrollments/
        # /enrollments/<int:pk>/
        # /enrollments/create/
        # /enrollments/update/<int:pk>/
        # /enrollments/delete/<int:pk>/

    Administration
        # /Smudge/

