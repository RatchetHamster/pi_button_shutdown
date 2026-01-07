FROM python:3.13.5
ADD main.py .
RUN pip install gpiozero rpi-lgpio
CMD ["python", "./main.py"]



