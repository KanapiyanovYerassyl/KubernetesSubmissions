import time
import uuid
from datetime import datetime, timezone
 

random_string = str(uuid.uuid4())
 
 
def log_line():
    timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    print(f"{timestamp}: {random_string}", flush=True)
 
 
def main():
    while True:
        log_line()
        time.sleep(5)
 
 
if __name__ == "__main__":
    main()