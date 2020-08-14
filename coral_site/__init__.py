from django.db.backends.signals import connection_created
def write_ahead_mode(sender, connection, **kwargs):
    """muda o modo de journaling pra write-ahead logging"""
    if connection.vendor == 'sqlite':
        cursor = connection.cursor()
        cursor.execute('PRAGMA journal_mode=WAL;')

connection_created.connect(write_ahead_mode)
