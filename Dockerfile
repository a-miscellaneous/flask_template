# Use a suitable base-image.
FROM python:3.13.1
RUN apt-get update && apt-get upgrade -y 


# Copy our service
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY main.py /
COPY gunicorn.conf.py /
COPY src/ /src/
# Run the service
ENTRYPOINT ["gunicorn", "-c" ,"gunicorn.conf.py", "main:app"]

