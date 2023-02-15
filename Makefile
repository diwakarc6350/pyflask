prune:
	docker system prune -a
docker-build:
	docker build . -t weather-app
docker-run-as-deamon:
	docker run -p 5000:5000 weather-app:latest -d
docker-run:
	docker run -p 5000:5000 weather-app:latest
tests:
	pytest ./test_app.py
start-app:
	python3 app.py 

