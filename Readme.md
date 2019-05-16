# Research-purpose_Logger
This is a research-purpose logger that helps in the code and config files organization, and massive result analysis for many abstraction level. Mainly, where large and exhausting experiments and/or manual hyperparameters selection are performed. I employed this logger in at least 6 private projects and 2 academic projects.


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
gpu 0: $ python training_net.py # Config files: the **fisrt** modification is done and the **first** configuration is saved
gpu 1: $ python training_net.py # Config files: the **second** modification is done and the **second** configuration is saved
gpu 1: $ python training_net.py # Config files: the **third** modification is done and the **third** configuration is saved
gpu 1: $ python training_net.py # Config files: the **fourth** modification is done and the **fourth** configuration is saved
```

Incorrect form...

```
gpu 0: [1] run training_net.py # Config files: the **fisrt** modification is done and the **first** configuration is saved
gpu 1: [2] run training_net.py # Config files: the **second** modification is done and the **first** configuration is saved
gpu 1: [3] run training_net.py # Config files: the **third** modification is done and the **first** configuration is saved
gpu 1: [4] run training_net.py # Config files: the **fourth** modification is done and the **first** configuration is saved
```
