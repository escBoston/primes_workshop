FROM python:3.8.3-slim
COPY src/ ./src/
COPY data/ ./data/
RUN pip install pandas
RUN pip install sympy
WORKDIR /src/
CMD ["python", "run_char_stats.py"]
