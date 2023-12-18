import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get ('/')
def get_list():
    return [1,2,3,]

@app.get ('/contact', response_class = HTMLResponse)
def get_list():
    return """
          <html>
        <head>
            <title>HTML con Fastapi</title>
        </head>
        <body>
            <h1>El clasico Hola Mundo</h1>
        </body>
    </html>
    """
def run():
    store.get_categories()

if __name__ == "__main__" :
    run()