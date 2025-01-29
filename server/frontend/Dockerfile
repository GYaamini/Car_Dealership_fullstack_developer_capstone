FROM node:16

WORKDIR /app

# Copy the frontend files
COPY server/frontend /app/

RUN npm install
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
