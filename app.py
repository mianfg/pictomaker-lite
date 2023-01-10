from fastapi import FastAPI, status
from fastapi.responses import Response
from routers import router as v2

app = FastAPI(
    title="PictoMaker Lite",
    description="""
This is **PictoMaker Lite**, the API for PictoMaker. You can use **PictoMaker** at [pictomaker.mianfg.me](https://pictomaker.mianfg.me/).

###### Designed with ❤️ by [mianfg](https://mianfg.me)

---

#### Know more

* Know more about this API [here](https://mianfg.me/projects/pictomaker-lite).""",
    version="2.0",
    contact={
        'name': 'mianfg',
        'url': 'https://mianfg.me',
        'email': 'hello@mianfg.me'
    }
)

app.include_router(v2, prefix="/api/v2")

@app.get("/health-check")
async def health_check():
    # # TODO: check settings dependencies passing as args and kwargs
    # a = 5
    # try:
    #     assert 5 / 0
    # except Exception:
    #     app.state.logger.exception("My way or highway...")
    return Response(status_code=status.HTTP_200_OK)
