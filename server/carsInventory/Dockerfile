FROM node:18.12.1-bullseye-slim

ENV CURDIR=server/carsInventory/

RUN npm install -g npm@9.1.3

# ADD package.json .
# ADD app.js .
# ADD data/car_records.json .
# COPY . .

ADD ${CURDIR}/package.json .
ADD ${CURDIR}/app.js .
ADD ${CURDIR}/data/car_records.json .
COPY ${CURDIR}/. .

RUN npm install

EXPOSE 3050

CMD [ "node", "app.js" ]