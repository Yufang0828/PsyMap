__author__ = 'gzhengDu'
import web
from web.contrib.template import render_jinja

render = render_jinja(
    'page',
    encoding='utf-8'
)

urls = (
    '/', 'index',
    '/show', 'show'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return render.index()

class show:
    def POST(self):
        i = web.input2();
        return i.username+i.password

if __name__ == "__main__":
    app.run()

