FROM python:3.13.4-slim-bullseye

WORKDIR /app

# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

COPY ./src .

# RUN echo "Hello, World!" > index.html

# docker build -f Dockerfile -t pyapp .
# docker run -it pyapp

CMD ["python", "-m", "http.server", "8000"]
