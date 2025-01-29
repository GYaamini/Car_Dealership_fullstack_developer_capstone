#######
#stage1
#######
FROM node:20-alpine as Build
WORKDIR /frontend

COPY server/frontend/. .

RUN npm install
RUN npm run build

#######
#stage2
#######
FROM node:20-alpine AS production
COPY --from=Build /frontend /frontend
EXPOSE 80
