from flask import Flask, render_template
from core.article import read_articles
from flask import request
from config import urls
import json
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/<feed>')
def list_articles(feed=''):
    articles = read_articles(feed, 20)
    update = datetime.now().replace(minute=0, second=0,microsecond=0).strftime("%Y-%m-%d, %H:%M")
    return render_template('list.html', articles=articles, feed=feed, urls=urls, update=update)

if __name__ == "__main__":
        app.run(host='0.0.0.0')
