FROM python:3.12-slim

ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

RUN python -m venv $VIRTUAL_ENV

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Draai niet als root; groep dialout geeft toegang tot seriële poorten
RUN useradd --system --no-create-home --groups dialout dsmr \
    && chown -R dsmr /app
USER dsmr

CMD ["python", "dsmr-mqtt.py"]
