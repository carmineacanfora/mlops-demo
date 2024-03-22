from transformers import TRANSFORMERS_CACHE
print(TRANSFORMERS_CACHE)

import shutil
shutil.rmtree(TRANSFORMERS_CACHE)