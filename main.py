import sys
import subprocess
import importlib.util
import locale
from collections import Counter

def load_student_function():
    """加载学生函数"""
    try:
        # 动态导入学生模块
        spec = importlib.util.spec_from_file_location("student_module", "main.py")
        if spec is None:
            return None, "❌ 错误: 找不到main.py文件"
        
        student_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_module)
        
        # 检查函数是否存在
        if not hasattr(student_module, 'analyze_text'):
            return None, "❌ 错误: main.py中没有定义analyze_text函数"
        
        return student_module.analyze_text, None
        
    except FileNotFoundError:
        return None, "❌ 错误: 找不到main.py文件"
    except SyntaxError as e:
        return None, f"❌ 语法错误: {e}"
    except Exception as e:
        return None, f"❌ 加载学生模块时出错: {e}"

def test_analyze_text(analyze_text):
    """测试文本分析功能"""
    test_cases = [
        # (输入文本, 预期频率字典)
        ("hello", {'l': 2, 'h': 1, 'e': 1, 'o': 1}),
        ("Hello World", {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}),
        ("Mississippi", {'s': 4, 'i': 4, 'p': 2, 'm': 1}),
        ("你好世界", {'你': 1, '好': 1, '世': 1, '界': 1}),
        ("", {}),
        ("123!@#", {}),
        ("a a a a", {'a': 4}),
    ]
    
    passed = 0
    total = len(test_cases)
    
    print("\n=== 文本分析功能测试 ===")
    
    for i, (input_text, expected_freq) in enumerate(test_cases):
        try:
            # 调用学生的analyze_text函数
            result = analyze_text(input_text)
            
            if not isinstance(result, (list, tuple)):
                print(f"❌ 测试 #{i+1} 失败: '{input_text}'")
                print(f"   错误: 函数应返回列表或元组，但返回了 {type(result)}")
                continue
            
            # 创建实际应该出现的字符频率字典（小写处理）
            expected_chars_lower = {}
            for char in input_text:
                if char.isalpha():
                    char_lower = char.lower()
                    expected_chars_lower[char_lower] = expected_chars_lower.get(char_lower, 0) + 1
            
            # 验证结果中的字符是否都在预期中
            valid = True
            error_msg = ""
            
            # 检查是否包含所有预期字符
            for expected_char in expected_chars_lower:
                if expected_char not in result:
                    valid = False
                    error_msg = f"缺少字符 '{expected_char}'"
                    break
            
            # 检查排序是否正确（降序）
            if valid and len(result) > 1:
                # 获取每个字符的频率
                char_freqs = []
                for char in result:
                    if char in expected_chars_lower:
                        char_freqs.append(expected_chars_lower[char])
                    else:
                        # 如果字符不在预期中，频率为0
                        char_freqs.append(0)
                
                # 检查是否降序排列
                for j in range(1, len(char_freqs)):
                    if char_freqs[j] > char_freqs[j-1]:
                        valid = False
                        error_msg = f"排序错误: 位置{j}的频率({char_freqs[j]}) > 位置{j-1}的频率({char_freqs[j-1]})"
                        break
            
            if valid:
                passed += 1
                print(f"✅ 测试 #{i+1} 通过: '{input_text}'")
            else:
                print(f"❌ 测试 #{i+1} 失败: '{input_text}'")
                print(f"   错误: {error_msg}")
                print(f"   预期字符: {list(expected_chars_lower.keys())}")
                print(f"   实际结果: {list(result)}")
                
        except Exception as e:
            print(f"💥 测试 #{i+1} 异常: '{input_text}'")
            print(f"   错误: {e}")
    
    score = int((passed / total) * 70) if total > 0 else 0
    print(f"\n功能测试得分: {score}/70 (通过 {passed}/{total} 个测试)")
    return score

def test_main_program():
    """测试学生的主程序交互"""
    try:
        # 设置超时防止无限循环
        timeout_seconds = 10
        
        # 测试输入数据
        test_input = "Hello World\n\n"  # 输入文本后跟空行
        
        # 运行主程序
        result = subprocess.run(
            [sys.executable, "main.py"],
            input=test_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            timeout=timeout_seconds
        )
        
        output = result.stdout
        
        # 检查是否有输出
        if not output or not output.strip():
            print("❌ 主程序没有输出")
            return 0
        
        print("\n=== 主程序输出（前500字符）===")
        print(output[:500] + "..." if len(output) > 500 else output)
        
        # 基础评分
        score = 0
        max_score = 30
        
        # 检查关键内容
        checks = [
            ("欢迎信息", 5, lambda x: any(word in x.lower() for word in ["文本", "字符", "频率", "分析"])),
            ("输入提示", 5, lambda x: any(word in x.lower() for word in ["输入", "请输入", "文本"])),
            ("分析结果", 10, lambda x: any(word in x.lower() for word in ["字符", "频率", "排序", "降序"])),
            ("实际分析", 10, lambda x: "l" in x.lower() and "o" in x.lower()),  # 检查是否真的分析了"Hello World"
        ]
        
        output_lower = output.lower()
        
        for check_name, points, check_func in checks:
            if check_func(output_lower):
                score += points
                print(f"✅ {check_name}: +{points}分")
            else:
                print(f"❌ {check_name}: 未通过")
        
        print(f"主程序测试得分: {score}/30")
        return score
        
    except subprocess.TimeoutExpired:
        print("❌ 主程序运行超时")
        return 0
    except Exception as e:
        print(f"❌ 主程序运行出错: {e}")
        return 0

def main():
    """主测试函数"""
    print("=" * 50)
    print("文本字符分析作业自动评分")
    print("=" * 50)
    
    # 加载学生函数
    analyze_text_func, error = load_student_function()
    if error:
        print(error)
        sys.exit(1)
    
    # 测试文本分析功能
    func_score = test_analyze_text(analyze_text_func)
    
    # 测试主程序交互
    main_score = test_main_program()
    
    # 计算总分
    total_score = func_score + main_score
    
    print("\n" + "=" * 50)
    print(f"最终得分: {total_score}/100")
    print("=" * 50)
    
    # 评分标准
    if total_score >= 90:
        print("🎉 优秀！")
    elif total_score >= 80:
        print("👍 良好！")
    elif total_score >= 70:
        print("✅ 及格！")
    elif total_score >= 60:
        print("⚠️ 勉强及格")
    else:
        print("💥 不及格")
    
    # 退出码
    sys.exit(0 if total_score >= 60 else 1)

if __name__ == "__main__":
    main()
