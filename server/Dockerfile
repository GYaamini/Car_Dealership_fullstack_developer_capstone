    FROM python:3.12.0-slim-bookworm

    ENV PYTHONBUFFERED 1
    ENV PYTHONWRITEBYTECODE 1
    
    # Change the workdir.
    WORKDIR /app

    # Install the requirements
    COPY ./requrements.txt /app/requirements.txt
    
    RUN pip install -r requirements.txt

    # Copy the rest of the files
    COPY . /app

    RUN ls
    
    EXPOSE 8000

    RUN chmod +x /app/entrypoint.sh

    ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

    CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
