import logging

from django.core.signals import request_finished
from django.dispatch import receiver

logger = logging.getLogger(__name__)

@receiver(request_finished)
def log_request_finished(sender, **kwargs):
    logger.info('Request finished.')
