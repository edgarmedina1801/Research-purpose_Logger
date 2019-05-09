# Research-purpose_Logger
This is research-purpose logger that helps on the organization of codes for several training and parameters. I employed this logger in at least 6 private projects and 2 academic projects.

## Usage

This code is flexible, some variables are easy to overwrite, in some cases config log or csv are needed, this type of files are generated automatically if dicts are employed.


```
import rlog_creator as rlog
from importlib import reload;reload(rlog) # not import for python2
rlog.save_log() # all variables must be filled correctly in the user space or written as local variables.
```

## Limitations.
Configuration files are not updated (reloaded) automatically, for consecutive experiments in different experiments the correct way is to call the main code on terminal, and not inside the ipython environment. It means... if a second process is run after first one in the same ipython. The saved configs files will be the first-run file.

Correct form...

```
gpu 0: $ python training_net.py # Config files: the <b>fisrt</b> modification is done and the <b>first</b> configuration is saved
gpu 1: $ python training_net.py # Config files: the <b>second</b> modification is done and the <b>second</b> configuration is saved
gpu 1: $ python training_net.py # Config files: the <b>third</b> modification is done and the <b>third</b> configuration is saved
gpu 1: $ python training_net.py # Config files: the <b>fourth</b> modification is done and the <b>fourth</b> configuration is saved
```

Incorrect form...

```
gpu 0: [1] run training_net.py # Config files: the <b>fisrt</b> modification is done and the <b>first</b> configuration is saved
gpu 1: [2] run training_net.py # Config files: the <b>second</b> modification is done and the <b>first</b> configuration is saved
gpu 1: [3] run training_net.py # Config files: the <b>third</b> modification is done and the <b>first</b> configuration is saved
gpu 1: [4] run training_net.py # Config files: the <b>fourth</b> modification is done and the <b>first</b> configuration is saved
```
