from urllib.parse import urljoin
import logging.config
from collections import namedtuple

from flask import Flask, abort, redirect, render_template, url_for, request
from lxml import etree
import requests
import yaml

logging.config.dictConfig(yaml.safe_load("""
version: 1
formatters:
    simple:
        format: "%(module),[%(asctime)s]\n(module),%(message)s"
handlers:
    file_handler:
        class: logging.FileHandler
        filename: "flask_app.log"
        level: DEBUG
        formatter: simple
root:
    level: DEBUG
    handlers: [file_handler]
"""))

app = Flask(__name__)
# wsgi, PEP 3333
# format: "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"

WIKIPEDIA_BASE_URL = "https://en.wikipedia.org/"
WIKIPEDIA_SEARCH_URL_PATTERN = urljoin(
    WIKIPEDIA_BASE_URL,
    "/w/index.php?search={query}"
)


@app.route("/")
def welcome_page():
    return "Welcome to Mailikipedia Search Engine"


@app.route("/file_like_path")
def file_like_path():
    return "Hi!"


@app.route("/folder_like_path/")
def folder_like_path():
    return "Hi!"


@app.route("/hello")
@app.route("/hello/<string:username>")
@app.route("/hello/<string:username>/<int:num>")
def greetings(username="Vasya", num=10):
    if num > 20_000:
        return abort(404)

    if num > 10_000:
        return redirect(url_for("greetings", username=username, num=100))

    hello_string = "<br/>".join([f"Hello, {username}!"] * num)
    return hello_string


@app.route("/search")
def wiki_search():
    query = request.args.get("query")
    app.logger.debug("got query to Wikipedia: %s", query)

    wikipedia_response = requests.get(WIKIPEDIA_SEARCH_URL_PATTERN.format(
        query=query
    ))
    
    articles = parse_wikipedia_search_result(wikipedia_response.text)
    
    return render_template(
        "wikipedia_search.html", 
        wikipedia_query=query, 
        processing_time=1, 
        wikipedia_base_url=WIKIPEDIA_BASE_URL,
        top_articles=articles,
    )


def parse_wikipedia_search_result(html):
    root = etree.fromstring(html, etree.HTMLParser())
    all_li_articles = root.xpath("//li[@class='mw-search-result']")
    articles = []
        
    Article = namedtuple('Article', ['index', 'link', 'title', 'snippet'])
    for i, li_article in enumerate(all_li_articles):
        href = li_article.xpath(".//a[1]/@href")[0]
        title = li_article.xpath(".//a[1]/@title")[0]
        snippet = "".join(li_article.xpath(".//div[2]")[0].itertext())
        
        article = Article(
            i+1,
            href, 
            title, 
            snippet,
        )
        articles.append(article)

    return articles
    

@app.errorhandler(404)
def default_404_page(error):
    app.logger.debug("Got error message: %s", error)
    return render_template("404.html"), 404
