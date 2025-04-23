from pydantic import BaseModel
from typing import List

class MatchedItem(BaseModel):
    instrumentId: str
    symbol: str
    Confidence: float

class NewsInput(BaseModel):
    content: str
    Url: str
    DateKey: str

class Metadata(BaseModel):
    source: str
    priority: str

class RequestBody(BaseModel):
    status: str
    requestId: str
    timestamp: str
    data: NewsInput
    metadata: Metadata
    
class BatchRequestBody(BaseModel):
    requests: List[RequestBody]

class ResponseData(BaseModel):
    url: str
    date: str
    matchedItem: List[MatchedItem]

class ResponseBody(BaseModel):
    status: str
    statusCode: int
    data: ResponseData
    errors: dict
    timestamp: str
    requestId: str