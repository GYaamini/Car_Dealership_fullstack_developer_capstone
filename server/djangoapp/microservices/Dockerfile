#######
#stage1
#######
FROM python:3.9.18-slim-bookworm as Build

WORKDIR /microserivces

COPY server/djangoapp/microservices/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY server/djangoapp/microservices/. .
RUN ls

#######
#stage2
#######
FROM python:3.9.18-slim-bookworm as Production
WORKDIR /microservices

# Copy the Artifacts from stage1 (code + dependecies compiled = Artifact)
COPY --from=Build /microserivces /microservices
EXPOSE 5000
