import logging

from django.core.signals import request_finished
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from sales.models import Sale

logger = logging.getLogger(__name__)

@receiver(request_finished)
def log_request_finished(sender, **kwargs):
    print('Request finished.')

@receiver(pre_save, sender=Sale)
def log_sale_pre_save(sender, **kwargs):
    print('Sale about to save.')

@receiver(post_save, sender=Sale)
def log_sale_post_save(sender, **kwargs):
    print('Sale finished saving.')
