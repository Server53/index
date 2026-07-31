from .base import IdGenerator
from .numeric import IdGeneratorNumeric

id_generator: IdGenerator = IdGeneratorNumeric.setup()
