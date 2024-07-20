FROM python
RUN pip install flask
WORKDIR /home/myapp
COPY ./static ./static/
COPY ./templates ./templates/
COPY sample_app.py ./
EXPOSE 8080
CMD python3 ./sample_app.py
