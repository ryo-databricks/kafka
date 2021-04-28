#!/bin/bash

kafkaSvConf="config/server.properties"
publicIp=$(curl -s http://checkip.amazonaws.com)

# Replace Kafka Public IP in server.propeties
sed -i -r "s/^(advertised\.listeners\=PLAINTEXT:\/\/)([^:]+)(.+$)/\1$publicIp\3/" $kafkaSvConf

for ((i=0; i < 3; i++)); do
  # Zookeeper Health Check
  zkpCheck=$(lsof -i:2181)

  if [ ! "$zkpCheck" ]; then
    # Start Zookeepr
    bin/zookeeper-server-start.sh -daemon config/zookeeper.properties
    sleep 2
    ((i++))

  else
    if [ $i -eq 0 ]; then
      echo "Zookeeper is already running."

    else
      echo "Zookeeper started successfully."

    fi

    i=3

    for ((j=0; j<3; j++)); do
      # Kafka Health Check
      kfkCheck=$(lsof -i:9092)

      if [ ! "$kfkCheck" ]; then
        # Start Kafka
        bin/kafka-server-start.sh -daemon config/server.properties
        sleep 3
        ((j++))

      else
        if [ $j -eq 0 ]; then
          echo "Kafka is already running."

        else
          echo "Kafka started successfully."

        fi

        j=3

      fi
    done
  fi
done

if [ ! "$zkpCheck" ]; then
  echo "Failed to start Zookeeper."
fi

if [ ! "$kfkCheck" ]; then
  echo "Failed to start kafka."
fi
