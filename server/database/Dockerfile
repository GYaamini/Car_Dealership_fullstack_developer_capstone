FROM node:18.12.1-bullseye-slim

ENV CURDIR=server/database/

RUN npm install -g npm@9.1.3

# ADD package.json .
# ADD app.js .
# ADD review.js .
# ADD dealership.js .
# ADD data/dealerships.json .
# ADD data/reviews.json .
# COPY . .

ADD ${CURDIR}/package.json .
ADD ${CURDIR}/app.js .
ADD ${CURDIR}/review.js .
ADD ${CURDIR}/dealership.js .
ADD ${CURDIR}/data/dealerships.json .
ADD ${CURDIR}/data/reviews.json .
COPY ${CURDIR}/. .

RUN npm install

EXPOSE 3030

CMD [ "node", "app.js" ]