FROM python:latest
	
RUN apt-get update && apt-get -y upgrade && pip install flask && pip install mariadb 
	
WORKDIR /usr/src/app
COPY . .

EXPOSE 5000
	
CMD ["python","./web-page-script.py"]