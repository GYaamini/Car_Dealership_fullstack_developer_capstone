#######
#stage1
#######
FROM node:20-alpine as Build
WORKDIR /frontend

COPY server/frontend/. /frontend/

RUN npm install
RUN npm run build

#######
#stage2
#######
FROM nginx:stable-alpine AS production
COPY --from=build /frontend/build /usr/share/nginx/html
EXPOSE 80
