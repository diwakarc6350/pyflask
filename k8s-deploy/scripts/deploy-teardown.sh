#!/bin/bash

kubectl -n default scale --replicas=0 deployment/weather-app 
kubectl -n default delete service/weather-app 
kubectl -n default delete deployment.apps/weather-app