
import os
import time
import uvicorn, json, datetime
from asgiref.sync import sync_to_async
from fastapi import FastAPI, File, UploadFile,  Request, Form

import os

def predict():
    import time 
    time.sleep(5)

def init_flask():

    app = FastAPI()

    # @app.get("/login")
    # async def login(request: Request):
    #     # config = json.loads(request.json)
    #     json_post_raw = await request.json()
    #     print(json_post_raw)
    #     config = json.loads(json_post_raw)
    #     username = config.get("username", "")
    #     password= config.get("password", "")
    #     # topp = config.get("top_p", 0.9)
    #     # t = config.get("temperature", 0.9)
    #     # seed = config.get("seed", 1000)
        
    #     # await sync_to_async(predict)()
    #     predict()
        
    #     result = {
    #         "code": 1,
    #         "msg": "login successfully",
    #         "data": {
    #             "stutas": "普通用户",
    #             "name": "测试用户",
    #         }
    #     }
    #     return result

    @app.get("/login")
    async def login(username: str, password: str):
        # print(request)
        # print(request.json)
        # config = json.loads(request.json)
        # print(config)
        # json_post_raw = await request.json()
        # print(json_post_raw)
        # # config = json.loads(json_post_raw)
        # username = config.get("username", "")
        # password= config.get("password", "")
        # topp = config.get("top_p", 0.9)
        # t = config.get("temperature", 0.9)
        # seed = config.get("seed", 1000)
        
        # await sync_to_async(predict)()
        # predict()
        print(username, password)
        
        result = {
            "code": 1,
            "msg": "login successfully",
            "data": {
                "stutas": "普通用户",
                "name": "测试用户",
            }
        }
        return result

    @app.post("/uploadfile/")
    async def create_upload_file(file: UploadFile):
        return {"filename": file.filename}

    @app.post("/files/")
    async def create_file(file: bytes = File(...)):
        return {"file_size": len(file)}


    return app 

app = init_flask()

uvicorn.run(app, host='0.0.0.0', port=5051, workers=1)