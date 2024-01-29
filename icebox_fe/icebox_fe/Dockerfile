FROM node:20.10.0-alpine3.18
WORKDIR /icebox_fe
COPY package.json package-lock.json ./
RUN npm install
RUN npm uninstall webpack-dev-server
COPY . ./
EXPOSE 3000
CMD ["npm", "start"]