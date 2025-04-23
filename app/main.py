from fastapi import FastAPI
from app.ner import process_ner, process_ner_batch
from app.models import BatchRequestBody, RequestBody, ResponseBody
from contextlib import asynccontextmanager
import datetime

app = FastAPI()

# Global variables to hold the model and tokenizer
model = None
tokenizer = None

# Function to load the model at startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML models here

    print("NER model loaded successfully!")


@app.post("/ner", response_model=ResponseBody)
async def ner_endpoint(request: RequestBody):
    timestamp = datetime.datetime.now().isoformat()
    matched_items = process_ner(request.data.content)
    
    # Start sample response
    response_data = {
        "url": request.data.Url,
        "date": request.data.DateKey,
        "matchedItem": matched_items
    }

    return ResponseBody(
        status="success",
        statusCode=200,
        data=response_data,
        errors={"code": None, "details": [], "suggestion": None},
        timestamp=timestamp,
        requestId=request.requestId
    )
    # End sample response


@app.post("/ner/batch", response_model=list[ResponseBody])
async def ner_batch_endpoint(batch_request: BatchRequestBody):
    timestamp = datetime.datetime.now().isoformat()
    matched_items = process_ner_batch(batch_request.requests)
    
    return None