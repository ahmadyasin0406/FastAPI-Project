# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

#app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://ahmadyasin:123@cluster0.xw4usgg.mongodb.net")


# @app.get("/", response_class=HTMLResponse)
# async def read_item_html(request: Request):
#     docs = conn.notes.notes.find({})
#     newDocs = []
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#         })
#         print(docs)
#     return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


# @app.get("/api/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}