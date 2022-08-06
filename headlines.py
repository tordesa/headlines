import feedparser

from flask import Flask

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"


@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]

    return f"""
    <html>
        <body>
            <h1>BBC Headlines</h1>
            <b>{first_article.get("title")}</b><br/>
            <i>{first_article.get("published")}</i><br/>
            <p>{first_article.get("summary")}</p><br/>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(port=5000, debug=True)
