import time

def hello():
  now = time.strftime("%c")
  return now

app = Flask(__name__)

@app.route('/')
def index():
  return hello()

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
