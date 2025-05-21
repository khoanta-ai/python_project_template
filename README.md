# Dự Án Mẫu Python

Dự án này minh họa cấu trúc thư mục tiêu chuẩn cho một dự án Python.

## Cấu trúc thư mục

- `src/`: Chứa mã nguồn chính
- `tests/`: Chứa các bộ kiểm thử
- `docs/`: Tài liệu hướng dẫn
- `resources/`: Tài nguyên (dữ liệu, template, ...)

## Ví dụ cực đơn giản

```python
# src/calc.py
def add(a: float, b: float) -> float:
    """Cộng hai số a và b."""
    return a + b

if __name__ == "__main__":
    print("Tổng của 2 và 3 là:", add(2, 3))
```

## Hướng dẫn chạy ví dụ

```bash
python src/calc.py
```

## Hướng dẫn kiểm thử

```bash
python -m unittest discover tests
```

## Tài nguyên mẫu

File `resources/sample_data.txt` chứa các cặp số để cộng:

```
2,3
-1,1
5,7
``` 