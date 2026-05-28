from .content import MAX_GENERAL, MAX_HEAVY_M


def validate_and_parse(inputs, param_names, func_name):
    parsed = []
    for text_field in inputs:
        value = (text_field.value or "").strip()
        if value == "":
            return False, "请填写所有输入项"
        if value == "-":
            return False, "请输入有效整数"

        try:
            parsed.append(int(value))
        except ValueError:
            return False, "请输入整数格式，不要包含其他字符"

    for name, value in zip(param_names, parsed):
        if name in ("m", "p") and value <= 0:
            return False, f"参数 {name} 必须为正整数"
        if abs(value) > MAX_GENERAL:
            return False, f"输入 {name} 的绝对值过大，建议 <= {MAX_GENERAL}"
        if func_name == "原根计算" and name == "m" and value > MAX_HEAVY_M:
            return False, f"原根计算请确保 m <= {MAX_HEAVY_M}，否则可能非常耗时"

    return True, parsed
