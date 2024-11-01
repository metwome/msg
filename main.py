from fastapi import FastAPI, Body
from starlette.responses import JSONResponse


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def main():
  return JSONResponse({'data': 'ok'}, status_code=200)

