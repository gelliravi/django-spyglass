from django.conf import settings

def add_users():
    return getattr(settings, 'SPYGLASS_ADD_USERS', False)

def conditionally(dec, cond):
     def resdec(f):
         if not cond:
             return f
         return dec(f)
     return resdec

# Receive the metamodel class from settings.METAMODEL
def get_meta():
    package = ".".join(settings.METAMODEL.split('.')[:-1])
    modelclass = settings.METAMODEL.split('.')[-1]
    Metamodel = __import__(package, globals(),locals(), [modelclass], -1)
    Metamodel = eval("Metamodel." + modelclass)
    return Metamodel

