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
        print(f"  {char}  |  {count}")# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    
    参数:
    text - 输入的字符串
    
    返回:
    list - 按字符频率降序排列的字符列表
    """
    # 在此处增加代码
    

# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("====================")
    print("请输入一段文本（输入空行结束）：")
    
    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    # 合并输入文本
    text = "\n".join(lines)
    
    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)
        
        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
        
        # 提示用户比较不同语言
        print("\n提示: 尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
