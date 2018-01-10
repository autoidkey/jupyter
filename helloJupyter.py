
# coding: utf-8

# In[14]:

import subprocess
subprocess.run(['jupyter', 'nbconvert', '--to', 'python', 'helloJupyter.ipynb'])


# In[11]:

your_name = "jupyter"

def hello(name):
    print("hey {0}".format(name))
    
hello(your_name)


# In[5]:

hello("note")


# your_name? #decstring  shift+tab is ok, too.

# !ls #unix command

# %pwd # provided by ipython kernel
