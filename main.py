from flask import Flask
from multiprocessing import Process
import json
import time
import os

app = Flask(__name__)

if os.path.isfile("test.txt"):
	os.remove("test.txt")

@app.route('/')
def home():
	try:
		with open("test.txt", "r") as f:
			return "<pre>" + f.read() + "</pre>"
	except:
		return 'poggers'

def test_job(t):
	for i in range(100):
		with open("test.txt", "a") as f:
			data =  f"[{i}][{t}]"
			print(data)
			f.write(data + "\n")
		time.sleep(1)

@app.route('/test')
def test():
	p = Process(target=test_job, args=(time.time(),))
	p.daemon = True
	p.start()

	return "ok"

if __name__ == "__main__":
	app.run("0.0.0.0", port=8000)
