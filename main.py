import uvicorn

def start(): 
    uvicorn.run(app='app:app', reload=True, port=5000)

if __name__ == '__main__':
    start()