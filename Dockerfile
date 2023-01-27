
FROM python:3
ADD calculator-app.py /calculator-app.py
ENTRYPOINT ["python","./calculator-app.py"]