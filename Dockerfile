ARG VERION_NAME=python:alpine
FROM ${VERION_NAME}

WORKDIR /app

COPY . /app

RUN pip install  nltk

# Download NLTK resources (including stopwords corpus)
RUN python -m nltk.downloader stopwords

CMD python WordFrequencyAnalysis.py