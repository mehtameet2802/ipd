import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello, World'}


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
# uvicorn main:app --reload
