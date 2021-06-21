# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler
import urllib.request
from bs4 import BeautifulSoup

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url = "https://qiita.com/"
    f = urllib.request.urlopen(url)
    html = f.read().decode('utf-8')

    soup = BeautifulSoup(html, "html.parser")
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(soup.encode(encoding='utf_8'))
    return

