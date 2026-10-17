def greet(name: str) -> str:
    """打个招呼。"""
    return f"你好，{name}！"


if __name__ == "__main__":
    print(greet("世界"))