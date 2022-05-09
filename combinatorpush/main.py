from deta import app

from env_data import EnvData
from utility.email import send_email

import requests

# define a function to run on a schedule
# the function must take an event as an argument
@app.lib.cron()
def cron_job(event):
    env_data = EnvData()

    response = requests.get("https://urmkmk.deta.dev/articles/5/")
    links = response.json()

    res = "<h1>YCombinator Top Links</h1>"

    for link in links:
        current_link = create_html_link(link["title"], link["url"])
        res = res + current_link + "<br>"
    
    send_email(res, env_data)
    return 200

def create_html_link(title, url):
    return "<a href=" + url + ">" + title + "</a>"

