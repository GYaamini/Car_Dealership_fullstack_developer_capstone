FROM node:18.12.1-bullseye-slim

RUN npm install -g npm@9.1.3

ADD server/database/package.json .
ADD server/database/app.js .
ADD server/database/review.js .
ADD server/database/dealership.js .
ADD server/database/data/dealerships.json .
ADD server/database/data/reviews.json .
COPY server/database/. .
RUN npm install

EXPOSE 3030

CMD [ "node", "app.js" ]
