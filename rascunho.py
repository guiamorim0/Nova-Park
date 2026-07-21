from datetime import datetime, timedelta
import math


agora = datetime.now()
print(agora)                          # o que sai?
print(agora.strftime("%H:%M"))       # e agora?
antes = agora - timedelta(hours=2)   # 2 horas atrás
diferenca = agora - antes            # subtração de datetimes!
print(diferenca.total_seconds())     # segundos da diferença

from datetime import datetime, timedelta

agora = datetime.now()
antes = agora - timedelta(hours=2)
diferenca = agora - antes
print(diferenca.total_seconds())

print(math.ceil(1.17))