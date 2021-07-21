FROM python
COPY pyproject.toml .
COPY /app/ app/
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install
CMD python app/bot.py