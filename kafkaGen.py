import sys, time, json, time, random, string
from argparse import ArgumentParser
from datetime import datetime
from kafka import KafkaProducer

def randomname(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def get_option(topic, num):
    argparser = ArgumentParser(description='This script generates JSON for Kafka stream with multipl
e topic')
    argparser.add_argument('-t', '--topic',
                           default=topic,
                           help='''
                                Specify name of topic. Topic Name will be topic1,topic2... \n
                                Default: topic\n
                                ''')
    argparser.add_argument('-n', '--num', type=int,
                           default=num,
                           help='''
                                Specify number of topic.\n
                                Default: None\n
                                ''')
    return argparser.parse_args()


def main():
    TOPIC_NAME = 'topic'
    NUM_OF_TOPIC = 1

    args = get_option(TOPIC_NAME, NUM_OF_TOPIC)
    t = str(args.topic)
    n = args.num + 1

    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    while True:
        if n is 1:
            topic = t
        else:
            topic = t + str(random.randrange(1, n, 1))
 
        id = random.randrange(1000)
        utime = int(time.time())
        word = randomname(5)
        val1 = randomname(15)
        val2 = random.choice(('hoge', 'fuga', 'piyo'))

        value = {
            "id" : id,
            "utime" : utime,
            "word": word,
            "val1": val1,
            "val2": val2
        }

        msg = json.dumps(value)
        producer.send(topic, msg.encode("utf-8"))
        producer.flush()
        print(str(topic) + "::" + str(msg))

        time.sleep(3)

if __name__ == '__main__':
    main()
