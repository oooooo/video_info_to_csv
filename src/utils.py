# utils.py
import os
import shutil  # 處理「檔案與資料夾的複製、刪除、壓縮、移動」等操作，比 os 更方便。


def list_files(directory, ext):
    """列出資料夾指定副檔名檔案"""
    try:
        return [f for f in os.listdir(directory) if f.endswith(ext)]
    except FileNotFoundError:
        print(f":: ❌ 錯誤: 找不到資料夾 '{directory}'")
        return []


def move_file(src, dst_dir):
    """移動檔案到目標資料夾"""
    os.makedirs(dst_dir, exist_ok=True)
    dst_path = os.path.join(dst_dir, os.path.basename(src))
    shutil.move(src, dst_path)
    return dst_path
