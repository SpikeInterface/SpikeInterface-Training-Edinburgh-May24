# SpikeInteface-Training-Edinburgh-May24

Material for user training day of SpikeInterface

TODO: put here some practical informations (venue, lunch, ...)


## schedule

**Morning : overiew and tutorials** 3.5h

* 9:00 - 10:00 Spike sorting overview (Pierre)
* 10:00 - 10:45 Spikeinterface overview (Alessio)
* break
* 11:00 - 11:20 Ultra quick demo with simulated (Sam)
* 11:20 - 12:30 Long and detailed on cambridge neurotech data (Sam)


**Afternoon : guided hands-on** 4h

Here the goal is to give details with guided hands-on.

* 14:00 - 14:15 object interaction cookbook (Ramon) Only talk (10-15)
* 14:15 - 14:30 probe handling (Zach)
* 14:30 - 14:50 preprocessing (Alessio)
* 14:50 - 15:10 drift with generated  (Pierre)
* 15:10 - 15:30 postprocessing (Chris) + plot matplolib
* break
* 15:50 - 16:10 visualization (Alessio sortingview and Sam sigui)
* 16:10 - 16:30 metrics and curation (automerge ? + reove duplicated) (Aurelien)
* 16:30 - 16:40 benchamark simulated  (Sam) Only talk
* 16:50 - 17:10 Export to NWB (ramon)
* break
* 16:30 - 16:50 benchmark simulated + hybrid + real with residual (Sam)
* 16:50 - 17:10 

Bonus track : 
* 17:30 - 18:30 Hand on on your own dataset + docker isntall
or
* 17:30 - 18:30 Container installation


=======


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
  * `python3.11 -m venv ~/.virtualenvs/si_env`
  * `source ~/.virtualenvs/si_env/bin/activate`
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
