# requirement.py
import sys
import subprocess
import os

def quick_generate():
    """一键生成 requirements.txt"""
    print("正在生成 requirements.txt...")
    
    # 方法1: 使用 pip freeze（推荐）
    with open('requires.txt', 'w') as f:
        # 添加 Python 版本
        f.write(f"# Python {sys.version}\n")
        f.write(f"python=={sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n\n")
        
        # 获取包列表
        subprocess.run([sys.executable, '-m', 'pip', 'freeze'], stdout=f)
    
    print("生成完成！")
    
    # 显示统计信息
    with open('requires.txt', 'r') as f:
        lines = f.readlines()
        package_count = len([l for l in lines if '==' in l]) - 1  # 减去 Python 本身
        print(f"包含 {package_count} 个包")

if __name__ == "__main__":
    quick_generate()