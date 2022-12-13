docker-compose down
docker container rm workshops_django_app_slave_1 workshops_django_app_master_1
sh ./init.sh
docker-compose up -d
