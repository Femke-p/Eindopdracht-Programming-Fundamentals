from datetime import datetime, timedelta
from color_text import *

def print_stripes():
    """Print een lijn met streepjes"""
    print(Style.RESET_ALL + 70 * "-")

def normal_time(timestamp, timezone_offset):
    """Zorgt ervoor dat een UTC-timestamp wordt omgezet naar de lokale tijd."""
    utc_time = datetime.utcfromtimestamp(timestamp)
    local_time = utc_time + timedelta(seconds=timezone_offset)
    return local_time.strftime('%d-%m-%y %H:%M:%S')