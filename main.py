def analyze_character_frequency(text):
    """
    分析字符串中字符的频率并按降序打印
    
    Args:
        text (str): 输入的字符串
    """
    # 创建字典来存储字符频率
    freq_dict = {}
    
    # 统计每个字符的出现次数
    for char in text:
        if char.isalpha():  # 只统计字母字符
            char_lower = char.lower()  # 不区分大小写
            freq_dict[char_lower] = freq_dict.get(char_lower, 0) + 1
    
    if not freq_dict:
        print("字符串中没有字母字符")
        return
    
    # 按频率降序排序
    sorted_chars = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    
    # 打印结果
    print(f"字符串: \"{text}\"")
    print("字符频率分析结果（按降序排列）:")
    print("-" * 40)
    print(f"{'字符':<6} {'频率':<8} {'百分比':<10}")
    print("-" * 40)
    
    total_chars = sum(freq_dict.values())
    
    for char, freq in sorted_chars:
        percentage = (freq / total_chars) * 100
        print(f"'{char}':    {freq:<8} {percentage:.2f}%")

def analyze_character_frequency_detailed(text, case_sensitive=False):
    """
    更详细的分析版本，可选择是否区分大小写
    
    Args:
        text (str): 输入的字符串
        case_sensitive (bool): 是否区分大小写
    """
    freq_dict = {}
    
    for char in text:
        if char.isalpha():
            if case_sensitive:
                key = char
            else:
                key = char.lower()
            freq_dict[key] = freq_dict.get(key, 0) + 1
    
    if not freq_dict:
        print("字符串中没有字母字符")
        return
    
    sorted_chars = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    total_chars = sum(freq_dict.values())
    
    print(f"字符串: \"{text}\"")
    print(f"分析模式: {'区分大小写' if case_sensitive else '不区分大小写'}")
    print("字符频率分析结果:")
    print("-" * 50)
    print(f"{'字符':<8} {'频率':<10} {'百分比':<12} {'条形图':<20}")
    print("-" * 50)
    
    max_freq = sorted_chars[0][1]
    
    for char, freq in sorted_chars:
        percentage = (freq / total_chars) * 100
        # 创建简单的条形图
        bar_length = int((freq / max_freq) * 20)
        bar = '█' * bar_length
        
        print(f"'{char}':     {freq:<10} {percentage:>6.2f}%     {bar}")

# 测试示例
if __name__ == "__main__":
    # 测试用例
    test_strings = [
        "Hello World!",
        "Programming is fun!",
        "你好，Hello! 123",
        "aabbbcccdddeee",
        "The quick brown fox jumps over the lazy dog"
    ]
    
    for i, text in enumerate(test_strings, 1):
        print(f"\n测试用例 {i}:")
        print("=" * 60)
        analyze_character_frequency(text)
        print()
    
    # 详细版本测试
    print("详细分析示例（区分大小写）:")
    analyze_character_frequency_detailed("Hello World!", case_sensitive=True)
