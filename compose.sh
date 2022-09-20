# mkdir data
mkdir -p data
# delete auth.code file in data if exists
rm -f data/auth.code
# compose
sudo docker-compose up --build
# -d
