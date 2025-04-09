import uvicorn

def start(): 
    uvicorn.run(app='app:app', reload=True, port=1000)

if __name__ == '__main__':
    start()