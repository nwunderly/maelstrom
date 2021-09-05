docker run -d \
 --name johnmallard \
 --network prod \
 -v $PWD/logs:/johnmallard/logs \
 --restart unless-stopped \
 johnmallard