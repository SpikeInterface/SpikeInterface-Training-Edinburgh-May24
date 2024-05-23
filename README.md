# SpikeInterface-Training-Edinburgh-May24

Material for the SpikeInterface training day, part of the [Tools and Methods for Next Generation Electrophysiology Workshop](https://spikeinterface.github.io/spikeinterface-events/spikeinterface-workshop-2024/).

Taking place on Tuesday May 28th at the University of Edinburgh in the [Informatics Forum](https://informatics.ed.ac.uk/about/location), room G.07.

**To do before the training:**
1. Install SpikeInterface, using the [installation guide](#installation) below
2. Download the [dataset for the tutorials](#dataset)
3. Run the `pre_workshop_tests` notebook to make sure your installion is working properly

If you have any problems, find an expert on Monday.

## Schedule

| Time        | Topic                                   | Presenter(s)                   | Type         |
|:------------|:----------------------------------------|:-------------------------------|:-------------|
| **Morning** | **Overview and Tutorials** (3.5 hours) |                               |             |
| 9:00 - 10:00   | Spike sorting overview                   | Pierre                         | Talk         |
| 10:00 - 10:45  | Spikeinterface overview                   | Alessio                        | Talk         |
|             | _break_                                 |                               |             |
| 11:00 - 11:20  | Ultra quick demo (simulated)             | Sam                           | Demo         |
| 11:20 - 12:30  | Long demo (Cambridge Neurotech data)     | Sam                           | Demo         |
|             |                                       |                               |             |
| **Afternoon** | **Guided Hands-on** (4 hours)            |                               |             |
| 14:00 - 14:15  | Object interaction cookbook              | Heberto                        | Talk         |
| 14:15 - 14:30  | Probe handling                          | Zach                          | Hands-on     |
| 14:30 - 14:50  | Preprocessing                           | Alessio                        | Talk         |
| 14:50 - 15:10  | Drift with generated data              | Pierre                         | Talk         |
| 15:10 - 15:30  | Postprocessing                          | Chris                         | Hands-on     |
|             | _break_ (20 min)                        |                               |             |
| 15:50 - 16:10  | Visualization (Sortingview, Sigui)       | Alessio, Sam                   | Hands-on     |
| 16:10 - 16:30  | Metrics & Curation (Automerge, etc.)     | Aurelien                       | Hands-on     |
| 16:30 - 16:40  | Benchmark (simulated)                   | Sam                           | Talk         |
| 16:50 - 17:10  | Export to NWB (neuroconv)                | Heberto                        | Hands-on     |
|             | _break_ (20 min)                        |                               |             |
| **Bonus Track** |                                       |                               |             |
| 17:30 - 18:30  | Hands-on with your own dataset           |                               | Hands-on     | 


## Installation

**Procedure for Windows/Apple:**

If you already have anaconda/vscode installed jump to 4.

  * Step 1 : If your username/login has spaces and/or weird symbols, **YOU MUST** create
    a new user with a simpler name (no spaces, no symbols). Login with such a user name.
  * Step 2: download anaconda from here https://www.anaconda.com/download
    For Windows users (even though it is sometimes not recommended) we advise to check “Anaconda to your path”.
    It will help with vscode compatibility.
  * Step 3 : If you do not have a code editor we advise installing vscode.
    https://code.visualstudio.com/download.
    After installation, you can add the plugins “python” and “jupyter”
  * Step 4 : Go to this page https://github.com/SpikeInterface/SpikeInteface-Training-Edinburgh-May24
  * Step 5 : click on **"code"** (green button) and download the zip. Etxract the zip.
  * Step 6 : Open the anaconda prompt (a terminal).
  * Step 7 : go at the correct place where the zip is etracted.
    This command is a tip not the good one :`cd C:/users/myusername/where_the_zip_is`
  * Step 8 : create the python environement `conda env create -f spikeinterface_environment.yml`.
    This can take a while and download many paquets. This need bandwith.
    **Do not expect to do this during the tutorial**


**Procedure for linux ubuntu/debian style:**

anaconda on linux is sometimes messing a lot for new users.
Standard installation using system and pip are faster and easier to manage.
  
  * `sudo apt install python3.11 python3.11-venv python3.11-dev`
  * `mkdir ~/.virtualenvs`
  * `python3.11 -m venv ~/.virtualenvs/si_tutorial`
  * `source ~/.virtualenvs/si_tutorial/bin/activate`
  * `pip install --upgrade pip`
  * `pip install spikeinterface[full]`
  * `pip install PySide6`
  * `pip install jupyterlab`
  * `pip install https://github.com/NeuralEnsemble/python-neo/archive/master.zip`
  * `pip install https://github.com/SpikeInterface/spikeinterface/archive/main.zip`
  * `pip install https://github.com/SpikeInterface/spikeinterface-gui/archive/main.zip`
  * `pip install https://github.com/magland/sortingview/archive/main.zip`
  * `pip install https://github.com/NeuralEnsemble/ephyviewer/archive/master.zip`
  


## Dataset

Please download datasets from this link:

https://drive.google.com/drive/folders/17RlgsMLheW82IMLMgmTFifVACebDZ8X5?usp=sharing
