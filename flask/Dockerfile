#Creating a base image for the environment creation to run the API
FROM python:3.6.1-alpine 

#Change the working directory
WORKDIR /project

#Copying file from the Local 
ADD . /project

#Install the requirement file
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#run the api file
CMD ["pyhton","main.py"]
