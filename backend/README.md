To run backend in developer mode
```
docker-compose -f docker-compose.yaml -f docker-compose@dev.yaml up -d --build
```

To run backend in production mode
```
docker-compose -f docker-compose.yaml -f docker-compose@prod.yaml up -d --build
```

Virtual env
```
python -m venv venv
./venv/Scripts/activate (windows)
pip3 install -r requirements.txt
```