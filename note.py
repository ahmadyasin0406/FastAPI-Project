from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn
from models.note import Note         # <-- import your Pydantic model
from schemas.note import noteEntity  # <-- import your schema helper

note = APIRouter()
templates = Jinja2Templates(directory="templates")


# GET Request: saare notes dikhane ke liye
@note.get("/", response_class=HTMLResponse)
async def read_item_html(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),   # ObjectId to string
            "title": doc["title"],
            "desc": doc.get("desc", ""),
            "important": doc.get("important", False)
        })
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )


# POST Request: naya note insert karne ke liye

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["title"] = formDict.get("title", "")
    formDict["desc"] = formDict.get("desc", "")
    formDict["important"] = True if formDict.get("important") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"Success":True}


    # print(form)

# @note.post("/")
# def add_note(note: Note):
#     inserted = conn.notes.notes.insert_one(dict(note))
#     new_note = conn.notes.notes.find_one({"_id": inserted.inserted_id})
#     return noteEntity(new_note)      # return proper schema
