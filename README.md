# streamlitTemplate
 template app for streamlit platform

**running**
> streamlit run mainApp.py

---

## Structure pages

*mainApp*: main file to run

*page_debug*: in-app debugging information

*stInfrastructure*: useful wrappers for streamlit functions

## Content pages
in *pages* directory
example page:  *page_A_top*

---

## Docker

Either of two files can be used to build basic templates (structural files):

build *usual* image:

> docker build . -f dockerFiles/Dockerfile -t template-app

build *Cern usable* image (for use with openShift):

> docker build . -f dockerFiles/DockerfileCern -t template-app

An additional file is supplied to make use of additional content (based on *usual* template image). 
The procedure is as follows:

1. make a ''pages'' sub-directory

2. add files to directory (use prefix: ''page_'')

3. build *new* image (from ''pages'' parent directory)

> docker build . -f DockerfileUpdate -t new-app
