# get alpine images
FROM nginx:alpine

# Nginx will listen on this port
EXPOSE 8888

# Remove default NGINX Configuration and copy custom conf
RUN rm /etc/nginx/conf.d/default.conf
COPY test.conf /etc/nginx/conf.d