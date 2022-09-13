# Django-E-commerce

### Database Structure
![E-Com_DB](https://user-images.githubusercontent.com/108905313/189901922-e877a4a1-0b22-4ac4-82c1-c70d0ed47a6f.jpeg)
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/SoftCysec/Django-E-commerce.git
$ cd Django-E-commerce
```
Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip3` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`
