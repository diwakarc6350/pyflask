# What is Weather APP
Weather app gets the weather information for a location by calling a free
weather data provider https://goweather.herokuapp.com

# How to use Weather APP
Simply call the endpoint and provide the city name.

eg: `curl http://localhost:5000/weather?city=boston | jq`

You should see a response like this.
```
{
  "description": "Partly cloudy",
  "forecast": [
    {
      "day": "1",
      "temperature": "+9 °C",
      "wind": "24 km/h"
    },
    {
      "day": "2",
      "temperature": "+8 °C",
      "wind": "27 km/h"
    },
    {
      "day": "3",
      "temperature": "+14 °C",
      "wind": "17 km/h"
    }
  ],
  "temperature": "+11 °C",
  "wind": "19 km/h"
}
```

# Running the Application locally
make start-app and `curl http://localhost:5000/weather?city=boston | jq` 

# Running the Application locally in a docker container
1. `make docker-build`
1. `make docker-run` and `curl http://localhost:5000/weather?city=boston | jq` 

# Running Tests
`make tests`

# K8s

## Deploying and Testing in MiniKube

1. `minikube start`
1. `kubectl -n default apply -f ./k8s-deploy/weather-app.yaml`
1. `minikube service -all` weather-app endpoing url is displayed by minikube. See the K8s Testing.png image saved in assets folder. Get the weather-app URL and add `/weather?city=boston` to the url and curl it.

## Stopping the Weather App
`kubectl -n default scale --replicas=0 deployment/weather-app`

## Teardown the Weather App
```
kubectl -n default scale --replicas=0 deployment/weather-app 
kubectl -n default delete service/weather-app 
kubectl -n default delete deployment.apps/weather-app
```

FYI: https://goweather.herokuapp.com/weather/ sometimes goes down and become unavailable you will see 500 error.