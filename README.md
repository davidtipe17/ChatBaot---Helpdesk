## Initial Setup:

Clone repo

```
$ git clone https://github.com/davidtipe17/ChatBot-Helpdesk.git
```

create a virtual environment

```
$ cd ChatBot-Helpdesk
$ python -m venv venv
$ source venv/Scripts/activate
```

Install dependencies

```
$ pip install -r requirements.txt
```

Install nltk package

```
>>> nltk.download('punkt')
```

Train to ChatBot ->
This will dump data.pth file. And then run
the following command to test it in the console.

```
$ (venv) python train.py
```

Run the Flask environment

```
$ (venv) flask run
```

## Note
