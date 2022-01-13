FROM python:3.7-alpine
COPY src/ ./src/
COPY data/ ./data/
RUN pip install pandas
WORKDIR /src/
CMD ["python", "run_char_stats.py"]
