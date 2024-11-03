# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from comfyui_api.comfyui_handler import generate_image

app = FastAPI()

class ImageRequest(BaseModel):
    prompt: str

@app.post("/generate-image")
async def generate_image_api(request: ImageRequest):
    try:
        # 调用 comfyui_handler 中的 generate_image 函数
        result = await generate_image(request.prompt)
        return {"image": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 其他路由和功能可以在这里添加
