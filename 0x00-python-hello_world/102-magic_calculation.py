def magic_calculation(a, b):
    # 0 LOAD_CONST               1 (98)
    # 2 LOAD_FAST                0 (a)
    # 4 LOAD_FAST                1 (b)
    # 6 COMPARE_OP               0 (<)
    # 8 POP_JUMP_IF_FALSE       16
    # 10 LOAD_FAST                1 (b)
    # 12 LOAD_FAST                0 (a)
    # 14 BINARY_ADD
    # 16 RETURN_VALUE
    if a < b:
        return b + a
    else:
        return 98
