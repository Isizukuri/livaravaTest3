Test Task 3 Livarava
======

.. attention::

    To work needed python 2.7!


Quick start guide
-----------------

Clone.
++++++

.. code-block::

    $ git  clone git@github.com:Isizukuri/livaravaTest3.git
    $ cd livaravaTest3

Install virtualenv.
++++++++++++++++++++

.. code-block::

    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$

Install packages.
+++++++++++++++++

.. code-block::

    (venv)$ pip install -r requirements.txt



Synchronize.
++++++++++++

.. code-block::

    (venv)$ pwd
    /some/path/to/projects/livaravaTest3
    (venv)$ cd src/
    (venv)$ ./manage.py migrate
    (venv)$ ./manage.py createsuperuser
    (venv)$ ./manage.py loaddata notes_TextNote.json

Run.
++++

.. code-block::

    (venv)$ pwd
    /some/path/to/projects/livaravaTest3
    (venv)$ cd src/
    (venv)$ ./manage.py runserver
