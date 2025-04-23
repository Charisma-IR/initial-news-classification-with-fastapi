import asyncio

# Single processing function
def process_ner(content: str):
    # Start sample response
    matched_items = [
        {"instrumentId": "IRO1BTEJ0001", "symbol": "وتجارت", "Confidence": 0.987},
        {"instrumentId": "IRO1BMLT0001", "symbol": "وبملت", "Confidence": 0.932}
    ]
    return matched_items
    # End sample response

# Batch processing function
async def process_ner_batch(requests):
    return None
