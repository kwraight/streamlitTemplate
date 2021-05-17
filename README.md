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

## Adding content

An additional file is supplied to make use of additional content (based on *usual* template image).
The procedure is as follows:

1. make a ''pages'' sub-directory

2. add files to directory (use prefix: ''page_'')
  * add letter suffix to order pages: e.g. ''page_A_first.py'' file --> ''first'' page of webApp

---

## Running locally

Run webApp locally:

* run streamlit:
> streamlit run mainApp.py

* open browser at ''localhost:8501''

---

## Running via docker

Either of two files can be used to build basic templates (structural files):

build *usual* image:

> docker build . -f dockerFiles/Dockerfile -t template-app

build *Cern usable* image (for use with openShift):

> docker build . -f dockerFiles/DockerfileCern -t template-app

An additional file is supplied to make use of additional content (based on *usual* template image).
The procedure is as follows:

* build *new* image (from ''pages'' parent directory)

> docker build . -f dockerFiles/Dockerfile -t new-app

The build will copy files in the pages directory into the image and use these as content of the webApp.

* run container from image:

> docker run -p 8501:8501 new-app

* open browser at ''localhost:8501''

**NB** no volume sharing included at the moment
