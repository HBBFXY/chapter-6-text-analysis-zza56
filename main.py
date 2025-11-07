def analyze_char_frequency(text):
    """分析字符串中字符出现的频率，并按频率降序返回结果"""
    # 创建空字典存储字符频率
    freq_dict = {}
    
    # 遍历字符串中的每个字符
    for char in text:
        # 忽略空格（可选，如果需要统计空格可删除此条件）
        # if char == ' ':
        #     continue
        
        # 更新字符频率：存在则+1，不存在则初始化为1
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    # 按频率降序排序，频率相同则按字符升序排列
    sorted_chars = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_chars


if __name__ == "__main__":
    # 获取用户输入的字符串
    user_input = input("请输入要分析的字符串：")
    
    # 进行字符频率分析
    frequency_result = analyze_char_frequency(user_input)
    
    # 打印结果
    print("\n字符频率分析结果（按频率降序）：")
    print("字符 | 出现次数")
    print("-" * 15)
    for char, count in frequency_result:
        print(f"  {char}  |  {count}")
