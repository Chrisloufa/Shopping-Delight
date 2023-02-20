"""Checkout App"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """Checkout configuration class"""
    name = 'checkout'

    def ready(self):
        import checkout.signals
