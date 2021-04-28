# base image
FROM python:3.8

# exposing default port for streamlit
EXPOSE 8501

# copy over and install packages
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

# copying everything over
COPY *.py ./code/
COPY pages/*.py ./code/pages/

WORKDIR code

# match exposed port
CMD ["streamlit", "run", "mainApp.py","--server.port=8501"]
