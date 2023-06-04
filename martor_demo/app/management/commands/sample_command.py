from django.core.management.base import BaseCommand, CommandError
import logging
import random
import time

from app.models import Service

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Sample command that interacts with the Service Model and outputs a log"

    def add_arguments(self, parser):
        parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        logger.info("The command started")
        total_count = 300
        for i in range(0, total_count):
            service_text_id = str(random.randint(1, 100000))
            new_service = Service(text_identifier=service_text_id, status="New")
            new_service.save()
            
            num_services = Service.objects.count()
            logger.info(f"There are {str(num_services)} Services")
            time.sleep(3)

        logger.info("The command completed")
        #self.stdout.write("Command completed successfully")