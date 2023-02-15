#!/bin/bash

kubectl -n default scale --replicas=0 deployment/weather-app 