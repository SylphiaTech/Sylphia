import uuid
import time

class Session:
    def __init__(self):
        self.session_id = str(uuid.uuid4())
        self.start_time = time.time()
        self.data = {}

    def add_result(self, module, result):
        self.data[module] = result

    def get_summary(self):
        return {
            "session_id": self.session_id,
            "started_at": self.start_time,
            "modules": list(self.data.keys()),
            "results": self.data
        }