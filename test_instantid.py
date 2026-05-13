#!/usr/bin/env python3
import sys

def main():
    print("=" * 50)
    print("开始 InstantID 测试")
    print("=" * 50)

    # 测试 1：检查 Python 环境
    print(f"✓ Python 版本: {sys.version}")

    # 测试 2：检查 GPU
    try:
        import torch
        print(f"✓ PyTorch 版本: {torch.__version__}")
        print(f"✓ CUDA 可用: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"✓ GPU 设备: {torch.cuda.get_device_name(0)}")
    except ImportError:
        print("✗ PyTorch 未安装")
        return False

    # 测试 3：尝试导入关键依赖
    packages = ['diffusers', 'transformers', 'accelerate']
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"✓ {pkg} 导入成功")
        except ImportError:
            print(f"✗ {pkg} 导入失败")

    print("=" * 50)
    print("测试完成！")
    print("=" * 50)
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)