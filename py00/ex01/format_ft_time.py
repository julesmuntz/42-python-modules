import datetime
from decimal import Decimal
from time import strftime

epoch = datetime.datetime(1970,1,1,0,0,0)
seconds = (datetime.datetime.utcnow() - epoch).total_seconds()
print("Seconds since January 1, 1970:", f'{seconds:,}', "or", f"{Decimal(seconds):.2e}", "scientific notation")
print(strftime("%B %d %Y"))