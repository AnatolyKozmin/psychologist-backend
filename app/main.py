from fastapi import FastAPI

app = FastAPI(title='Backend for Telegram mini app',
              version='1.0.0')


@app.get('/')
async def root():
    return {"message": "FastAPI work...."}
