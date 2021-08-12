# streamlitTemplate
 template app for streamlit platform

 **Basic Idea:**
 * template for [streamlit](https://streamlit.io) webApps

 Check requirements file for necessary libraries

---

## Structure pages

*mainApp*: main file to run

## Core code
in *core* directory

*app*: app class and basic structure

*page*: page class and basic structure

*stInfrastructure*: useful wrappers for streamlit functions

## Core pages:
in *userPages* directory

*pageX*: Debug page _a.k.a._ "Broom Cupboard" containing session state settings

## User content pages:
in *userPages* directory

*page0*: example page

---

## Adding content

See example page for template structure.
The procedure is as follows:

1. make a ''userPages'' sub-directory

2. add files to directory (use prefix: ''page_'')
  * add number suffix to order pages: e.g. _page1.py_ name will be first in sidebar selection.

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

build image:

> docker build . -f dockerFiles/Dockerfile -t new-app

The build will copy files in the _userPages_ directory into the image and use these as content for the webApp.

* run container from image (mapping ports):

> docker run -p 8501:8501 new-app

* open browser at ''localhost:8501''

---

## Running with mounted volumes

This allows changes to files in mounted directory to be propagated to container immediately (*i.e.* without docker rebuilds) - useful for development!
**NB** this will overwrite any files in linked directory:

> docker run -p 8501:8501 -v $(pwd)/userPages:/code/userPages new-app
