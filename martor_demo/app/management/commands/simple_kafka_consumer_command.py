from django.core.management.base import BaseCommand, CommandError
import logging
import random
import time
from kafka import KafkaConsumer

from app.models import Service

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Simple kafka consumer"

    def handle(self, *args, **options):
        logger.info("The simple kafka consumer command started")

        consumer = KafkaConsumer(
            'simple_topic',
            bootstrap_servers=['kafka:29092'],
            group_id='simple_kafka_consumer_group',
            auto_offset_reset='earliest'
        )

        for message in consumer:
            value = message.value.decode('utf-8')
            logger.info(f"Received message: {value}")

            service_text_id = str(random.randint(1, 100000))
            new_service = Service(text_identifier=service_text_id+value, status="New")
            new_service.save()
            
            num_services = Service.objects.count()
            logger.info(f"There are {str(num_services)} Services")

        # total_count = 300
        # for i in range(0, total_count):
        #     service_text_id = str(random.randint(1, 100000))
        #     new_service = Service(text_identifier=service_text_id, status="New")
        #     new_service.save()
            
        #     num_services = Service.objects.count()
        #     logger.info(f"There are {str(num_services)} Services")
        #     time.sleep(3)

        logger.info("The command completed")
        #self.stdout.write("Command completed successfully")