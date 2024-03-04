FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./ 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:3000", "server:app"]
