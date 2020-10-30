
import time

def sleep(n_secs):
    time.sleep(n_secs)
def setup_hooks_prepare(request):
    return request.get("headers", {}).get("Location")
def change():
    pass