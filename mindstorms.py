import time
from cued_ia_lego import *

try:
    brick = LegoBrick()
except Exception:
    print("No brick found")
    exit()

