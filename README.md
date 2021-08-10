# streamlitTemplate
 template app for streamlit platform

 **Basic Idea:**
 * template for [streamlit](https://streamlit.io) webApps

 Check requirements file for necessary libraries

---

## Structure pages

*mainApp*: main file to run

## Content pages
in *pages* directory
example page:  *page0*

*page_debug*: in-app debugging information

*stInfrastructure*: useful wrappers for streamlit functions

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

* get required libraries:
> python3 -m pip install -r requirements

* run streamlit:
> streamlit run mainApp.py

* open browser at ''localhost:8501''

---

## Running via Docker

Either of two files can be used to build basic templates (structural files):

build *usual* image:

> docker build . -f dockerFiles/Dockerfile -t new-app

build *Cern usable* image (for use with openShift):

> docker build . -f dockerFiles/DockerfileCern -t new-app

An additional file is supplied to make use of additional content (based on *usual* template image).
The procedure is as follows:

* build *new* image (from ''pages'' parent directory)

> docker build . -f dockerFiles/Dockerfile -t new-app

The build will copy files in the pages directory into the image and use these as content of the webApp.

* run container from image:

> docker run -p 8501:8501 new-app

* open browser at ''localhost:8501''

---

## Running with mounted volume

This allows changes to files in mounted directory to be propagated to container immediately (*i.e.* without rebuilding) - useful for development!
**NB** this will overwrite any files in linked directory:

> docker run -p 8501:8501 -v $(pwd)/pages:code/pages new-app
