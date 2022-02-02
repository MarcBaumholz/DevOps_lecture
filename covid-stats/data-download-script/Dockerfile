FROM python:latest
	
RUN apt-get update && apt-get -y upgrade && pip install flask && pip install mariadb && pip install datefinder && pip install requests
	
WORKDIR /usr/src/app
COPY . .
	
CMD ["python","./data_download_script.py"]