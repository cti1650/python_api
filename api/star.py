from http.server import BaseHTTPRequestHandler
from datetime import datetime
import json
import random
import uuid
import time

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    result = json.dumps(
        {
            "id": str(uuid.uuid4()),
            "日付": time.strftime("%m/%d/%Y", time.localtime()) ,
            "ランダム値": random.sample(range(10),3),
            "確率": 0
        }, ensure_ascii=False)
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(result.encode(encoding='utf_8'))
    return
