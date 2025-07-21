from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from model import Transliterator

app = FastAPI()
transliterator = Transliterator("HoussemDegachi/arabix-small")

class TransliterateRequest(BaseModel):
    text: str

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
        return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({"detail": exc.detail}),
    )

@app.get("/transliterate")
async def transliterate(body: TransliterateRequest, status_code=status.HTTP_200_OK):
    print(f"New request: {body.text}")
    try:
        transliterated_text = transliterator.transliterate(body.text)
    except:
         raise HTTPException(status_code=500, detail="An error occured")       
    print(f"Response: {transliterated_text}")  
    return {"text": transliterated_text, "message": "Text transliterated successfully"}