#!/usr/bin/python3

result = 0
for i in range(1, 3):
    try:
        if i > a:
            raise Exception("Too far")
            result += a ** i / i
    except Exception:
        pass
    else:
        result += b
    finally:
        return result
