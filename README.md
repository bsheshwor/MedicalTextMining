
<br />
<div align="center">
  <img src="assets/logo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Text Mining on Medical Dataset</h3>

  <p align="center">
    This is a mini project done in order to mine useful information from medical data using the implication of fields like information retrieval, information extraction, natural language processing and artificial intelligence.
  </p>
</div>
<br>


## In order to execute the project:

First make a python virtual environment:

```
    $ python -m venv env
```


Then activate the virtual environment:

```
    For Windows: 
      $ ./env/Scripts/Activate.ps1 # for powershell
      $ ./env/Scripts/activate.bat # for Command Prompt
    For POSIX:
      $ source env/Scripts/Activate
```

Install the necessary python packages.
The required packages list is in *requirements.txt* file.

```
    $ python -m pip install -r requirements.txt
```

Apart from requirements.txt, some packages need to be installed manually using the commands.

```
    $ pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_ner_bc5cdr_md-0.5.1.tar.gz
 
    $ pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_ner_bionlp13cg_md-0.5.1.tar.gz
```

After the installation of the required libraries, we run the main python file:
```
    $ python main.py
```

The obtained json file is then pushed inside the database with following command:  
```
    $ python json2db.py
```

We have used the MongoDB database to store our data. So, the following things need to be installed:

<a href="https://www.mongodb.com/docs/manual/installation/">Install MongoDB</a>
<br/>
<a href="https://www.mongodb.com/docs/compass/current/install/">Download and install compass</a>



<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.



