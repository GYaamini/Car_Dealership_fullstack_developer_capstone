# Build Stage
FROM node:20-alpine as Build
WORKDIR /app/frontend

COPY server/frontend/. /app/frontend/

RUN npm install
RUN npm run build

# Production Stage
FROM nginx:stable-alpine AS production
COPY --from=build /app/frontend/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]