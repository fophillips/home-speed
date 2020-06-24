from python:3.8

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY home-speed.py .
CMD python home-speed.py
