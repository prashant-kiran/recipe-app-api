"""
Django command for database to be available.
"""
import time

from django.core.management.base import BaseCommand


from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database up"""

    def handle(self, *args, **options):
        """entry point for command."""
        self.stdout.write("waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("""Database unavailable
                                  waiting for 1 second...""")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
