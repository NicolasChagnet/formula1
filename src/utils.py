def convert_int_safe(s, default=0):
    """Returns int(s) if it is a valid integer, otherwise a default value"""
    try:
        val = int(s)
    except (ValueError, TypeError):
        val = default
    return val
