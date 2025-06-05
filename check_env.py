import importlib
import sys

def check_package(pkg):
    try:
        module = importlib.import_module(pkg)
        print(f"{pkg} version: {module.__version__}")
    except Exception as e:
        print(f"{pkg} not installed: {e}")
        return False
    return True

packages = ["paddleocr", "paddle"]
all_ok = True
for p in packages:
    if not check_package(p):
        all_ok = False

# check gpu
try:
    import paddle
    gpu_available = paddle.is_compiled_with_cuda() and paddle.device.cuda.device_count() > 0
    print("GPU Available:", gpu_available)
except Exception as e:
    print("Failed to check GPU via paddle:", e)
    all_ok = False

# simple bn test
if all_ok:
    try:
        from paddleocr import PaddleOCR
        ocr = PaddleOCR(lang='bn', use_angle_cls=False)
        print("Bangla language support loaded successfully")
    except Exception as e:
        print("Failed to initialize PaddleOCR with Bangla language:", e)

