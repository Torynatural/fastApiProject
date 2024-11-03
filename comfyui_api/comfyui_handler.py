# comfyui_handler.py

import subprocess


# comfyui_handler.py

import httpx

async def generate_image(prompt: str):
    """
    通过 HTTP 请求连接远程 ComfyUI 服务器生成图片
    """
    url = "http://117.129.59.184:8188/"  # 替换为实际的 ComfyUI 地址和端口
    payload = {"prompt": prompt}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()  # 检查请求是否成功
            return response.json()  # 返回生成图片的数据
    except httpx.HTTPStatusError as e:
        raise Exception(f"远程 ComfyUI 生成失败: {e.response.text}")
    except Exception as e:
        raise Exception(f"请求 ComfyUI 服务器时出错: {str(e)}")

