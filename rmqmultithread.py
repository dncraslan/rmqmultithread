import threading
import time
import pika
import random
import lorem

threads = []

def start_threads(thread_size,func_name):
	for i in range(thread_size):
		t = threading.Thread(target=func_name)
		threads.append(t)
		t.start()

def wait_for_search():
	for thread in threads:
		thread.join()       

def rmq_sender(category,content):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()        
        channel.queue_declare(queue=category)
        channel.basic_publish(exchange='',
                        routing_key=category,
                        body=content)
        print('\n [+]katagori ' + category + ' bilgisi = ' + content + ' geldi. ')
        connection.close()

def instagram_db_reciver():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='instagram')

        def callback(ch, method, properties, body):
                print("\n instagram bilgisi kaydedildi = " + body)

        channel.basic_consume(callback,
                        queue='instagram',
                        no_ack=True)
        print('\n [*] Waiting for instagram news.')
        channel.start_consuming()

def facebook_db_reciver():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='facebook')

        def callback(ch, method, properties, body):
                print("\n facebook bilgisi kaydedildi = " + body)

        channel.basic_consume(callback,
                        queue='facebook',
                        no_ack=True)
        print('\n [*] Waiting for facebook news.')
        channel.start_consuming()

def linkedin_db_reciver():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()        
        channel.queue_declare(queue='linkedin')

        def callback(ch, method, properties, body):
                print("\n linkedin bilgisi kaydedildi = " + body)

        channel.basic_consume(callback,
                        queue='linkedin',
                        no_ack=True)
        print('\n [*] Waiting for linkedin news.')
        channel.start_consuming()

def eksisozluk_db_reciver():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='eksisozluk')

        def callback(ch, method, properties, body):
                print("\n eksisozluk bilgisi kaydedildi = " + body)

        channel.basic_consume(callback,
                        queue='eksisozluk',
                        no_ack=True)
        print('\n [*] Waiting for eksisozluk news.')
        channel.start_consuming()

def blahaber_db_reciver():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='blahaber')

        def callback(ch, method, properties, body):
                print("\n blahaber bilgisi kaydedildi = " + body)

        channel.basic_consume(callback,
                        queue='blahaber',
                        no_ack=True)
        print('\n [*] Waiting for blahaber news.')
        channel.start_consuming()

def bot():
        medias = ['instagram','facebook','linkedin','eksisozluk','blahaber']
        media = random.choice(medias)
        sentence = lorem.sentence()
        rmq_sender(media,sentence)

start_threads(1,instagram_db_reciver)
start_threads(1,facebook_db_reciver)
start_threads(1,linkedin_db_reciver)
start_threads(1,eksisozluk_db_reciver)
start_threads(1,blahaber_db_reciver)

time.sleep(2)

start_threads(100,bot)

wait_for_search()