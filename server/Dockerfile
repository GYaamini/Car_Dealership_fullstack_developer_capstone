    FROM python:3.12.0-slim-bookworm

    ENV PYTHONBUFFERED 1
    ENV PYTHONWRITEBYTECODE 1
    

    # Change the workdir.
    WORKDIR /app

    # Install the requirements
    COPY server/requirements.txt requirements.txt

    RUN pip3 install -r requirements.txt

    # Copy the rest of the files
    COPY server/. ./

    # Run npm build
    FROM node:10-alpine as BUILD
    
    WORKDIR /app/frontend

    COPY server/frontend/. /app/frontend/
    
    RUN npm install
    RUN npm run build

    WORKDIR /app
    
    EXPOSE 8000

    RUN chmod +x /app/entrypoint.sh

    ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

    CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
