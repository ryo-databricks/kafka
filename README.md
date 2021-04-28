# Kafka JSON Streaming Generator


#### usage: genKafkaStream.py [-h] [-t TOPIC] [-n NUM]

This python script generates JSON for Kafka stream with multiple topic.  
Requires: Python >=3.0  

#### Example Usage:
$ python3 genKafkaSrteam.py -n 3  
topic1::{"id": 356, "count": 2, "utime": 1619596164, "word": "ZHmA4", "val1": "pW4qNeteIgx266C", "val2": "hoge"}  
topic3::{"id": 344, "count": 4, "utime": 1619596170, "word": "q1Edo", "val1": "ULcOuD3sSusQi3z", "val2": "piyo"}  
topic1::{"id": 922, "count": 5, "utime": 1619596173, "word": "9nnhM", "val1": "Dg8AQmxt7CBtlcJ", "val2": "piyo"}  
topic2::{"id": 616, "count": 6, "utime": 1619596176, "word": "A7FLS", "val1": "ZYCwPRAQjvfZHjV", "val2": "fuga"}  

#### Script Output Format:  
[ Topic Name ]::[{ JSON output to the stream }]  

#### JSON Stream Format:  
id - int, Randam 3 digits number  
count - int, Count up for each line of output  
utime - int, Unix time at which each line was generated  
word - string, Random 5 chars  
val1 - string, Random 15 chars  
val2 - string, Randomly selected from the following three strings [ hoge, fuga, piyo ]  

#### Optional arguments:  
~~~
    -h, --help  
        show this help message and exit.  
        
    -t TOPIC, --topic TOPIC  
        Specify name of topic. Topic Name will be topic1, topic2, ...  
        Default: topic
        
    -n NUM, --num NUM  
        Specify number of topic.  
        Default: 1  
~~~

