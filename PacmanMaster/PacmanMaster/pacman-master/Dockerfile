FROM --platform=$BUILDPLATFORM node:25-bullseye-slim as builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["node", "bin/server.js"]
