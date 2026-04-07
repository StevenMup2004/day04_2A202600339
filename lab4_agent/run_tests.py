import sys
from io import StringIO
from agent import graph

test_cases = [
    (
        "Test 1 - Direct Answer (Không cần tool)", 
        "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."
    ),
    (
        "Test 2 - Single Tool Call", 
        "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"
    ),
    (
        "Test 3 - Multi-Step Tool Chaining", 
        "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"
    ),
    (
        "Test 4 - Missing Info / Clarification", 
        "Tôi muốn đặt khách sạn"
    ),
    (
        "Test 5 - Guardrail / Refusal", 
        "Giải giúp tôi bài tập lập trình Python về linked list"
    )
]

def run_all_tests():
    with open("test_results.md", "w", encoding="utf-8") as f:
        f.write("# KẾT QUẢ TEST CAES - LAB 4\n\n")
        
        for name, query in test_cases:
            f.write(f"## {name}\n")
            f.write(f"**User:** `{query}`\n\n")
            f.write("**Log Console & Trả lời:**\n")
            f.write("```text\n")
            
            print(f"Đang chạy: {name} ...")
            
            # Chuyển hướng (redirect) print() thành chuỗi text thay vì in ra terminal
            old_stdout = sys.stdout
            captured_output = StringIO()
            sys.stdout = captured_output
            
            try:
                # Gửi request vào LangGraph (gửi list mỗi HumanMessage để giả lập hội thoại mới tinh, không có history)
                result = graph.invoke({"messages": [("human", query)]})
                final = result["messages"][-1]
                print(f"TravelBuddy: {final.content}")
            except Exception as e:
                print(f"[Lỗi trong quá trình chạy graph]: {e}")
                
            # Trả lại print() như cũ và ghi text bắt được vào markdown
            sys.stdout = old_stdout
            f.write(captured_output.getvalue().strip() + "\n")
            f.write("```\n\n")
            
    print("✅ Đã hoàn thành chạy các test cases! Kết quả được lưu tại file: test_results.md")

if __name__ == "__main__":
    run_all_tests()
