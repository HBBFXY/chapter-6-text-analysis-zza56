def analyze_text(text):
    """
    分析文本字符频率，按频率降序返回字符列表
    
    Args:
        text (str): 输入文本
        
    Returns:
        list: 按字符频率降序排列的字符列表
    """
    # 创建字典统计字符频率
    freq_dict = {}
    
    # 遍历文本中的每个字符
    for char in text:
        # 只统计字母字符（包括中英文）
        if char.isalpha():
            # 将字符转换为小写进行统计（可选，根据需求调整）
            char_lower = char.lower()
            freq_dict[char_lower] = freq_dict.get(char_lower, 0) + 1
    
    # 按频率降序排序，频率相同的按字符顺序排列
    sorted_chars = sorted(freq_dict.keys(), key=lambda x: (-freq_dict[x], x))
    
    return sorted_chars

def print_char_frequency(text):
    """
    打印字符频率分析结果
    
    Args:
        text (str): 输入文本
    """
    # 获取排序后的字符列表
    sorted_chars = analyze_text(text)
    
    if not sorted_chars:
        print("文本中没有字母字符")
        return
    
    # 重新统计频率用于显示
    freq_dict = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            freq_dict[char_lower] = freq_dict.get(char_lower, 0) + 1
    
    print(f"文本: \"{text}\"")
    print("字符频率分析结果（降序排列）:")
    print("-" * 40)
    
    for char in sorted_chars:
        frequency = freq_dict[char]
        print(f"字符 '{char}': 出现 {frequency} 次")

def main():
    """主程序：交互式文本分析"""
    print("=" * 50)
    print("文本字符频率分析器")
    print("=" * 50)
    
    while True:
        print("\n请输入要分析的文本（输入空行退出）:")
        user_input = input().strip()
        
        if not user_input:
            print("程序结束，谢谢使用！")
            break
        
        print_char_frequency(user_input)

# 测试用例
def test_analyze_text():
    """测试函数"""
    test_cases = [
        "hello",
        "Hello World",
        "Mississippi",
        "编程练习programming",
        "你好，世界！Hello World!",
        "123!@#",  # 无字母字符
        ""  # 空字符串
    ]
    
    for text in test_cases:
        print(f"\n测试文本: '{text}'")
        result = analyze_text(text)
        print(f"分析结果: {result}")

if __name__ == "__main__":
    # 运行测试
    test_analyze_text()
    
    # 运行交互式程序
    main()
