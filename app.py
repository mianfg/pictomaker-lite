from fastapi import FastAPI, status
from fastapi.responses import Response
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from routers import router as v2
from utils import docs


tags_metadata = [
    {
        "name": "Health",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "Generate",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    docs_url=None,
    redoc_url='/docs',
    openapi_tags=tags_metadata,
    contact={
        'name': 'mianfg',
        'url': 'https://mianfg.me',
        'email': 'hello@mianfg.me'
    },
)

app.include_router(v2, prefix="/api/v2")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health-check", tags=["Health"])
async def health_check():
    # # TODO: check settings dependencies passing as args and kwargs
    # a = 5
    # try:
    #     assert 5 / 0
    # except Exception:
    #     app.state.logger.exception("My way or highway...")
    return Response(status_code=status.HTTP_200_OK)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="PictoMaker Lite",
        version="v2.1",
        description=docs.description,
        routes=app.routes
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "/static/logos/logo-docs.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

def get_redoc_html(
    *,
    openapi_url: str,
    title: str,
    redoc_favicon_url: str = "https://fastapi.tiangolo.com/img/favicon.png",
    with_google_fonts: bool = True,
) -> HTMLResponse:
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{title}</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    """
    if with_google_fonts:
        html += """
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">
    """
    html += f"""
        <link rel="shortcut icon" href="{redoc_favicon_url}">
        <!--
        ReDoc doesn't change outer page styles
        -->
        <style>
          body {{
            margin: 0;
            padding: 0;
          }}
        </style>
        </head>
        <body>
            <div id="redoc-container"></div>
              <script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.55/bundles/redoc.standalone.min.js"> </script>
              <script src="https://cdn.jsdelivr.net/gh/wll8/redoc-try@1.4.1/dist/try.js"></script>
              <script>
                initTry({{
                openApi: `{openapi_url}`,
                  redocOptions: {{scrollYOffset: 50}},
                }})
              </script>
        </body>
        </html>
        """
    return HTMLResponse(html)


@app.get("/redoc", include_in_schema=False)
async def redoc_try_it_out():
    title = app.title + " Redoc with try it out"
    return get_redoc_html(openapi_url=app.openapi_url, title=title)