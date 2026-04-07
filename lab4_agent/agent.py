from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv

# Tải biến môi trường (OPENAI_API_KEY)
load_dotenv()

# 1. Đọc System Prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# 2. Khai báo State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 3. Khởi tạo LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    # Kiểm tra và thêm SystemMessage vào đầu danh sách nếu chưa có
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
        
    # === LOGGING KẾT QUẢ TOOL ===
    # Nếu tin nhắn cuối cùng là từ tool (tức là node 'tools' vừa chạy xong và truyền lại cho 'agent')
    if messages and messages[-1].type == "tool":
        tool_name = messages[-1].name
        tool_result = messages[-1].content
        print(f"[LOG] Kết quả trả về từ tool [{tool_name}]:\n{tool_result}\n" + "-"*40)
        
    response = llm_with_tools.invoke(messages)
    
    # === LOGGING ===
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"[LOG] LLM quyết định gọi tool: {tc['name']} với tham số {tc['args']}")
    else:
        print(f"[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng")
        
    return {"messages": [response]}

# 5. Xây dựng Graph
builder = StateGraph(AgentState)

# Khai báo các Nodes
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

# Định nghĩa luồng chạy (Edges)
# Bắt đầu luồng luôn là chạy Agent Node để suy nghĩ
builder.add_edge(START, "agent")

# Sử dụng conditional_edge được cung cấp sẵn (tools_condition)
# - Nếu response có tool_calls -> đi sang node "tools"
# - Nếu response ra text thuần -> đi tới kết thúc đồ thị (END)
builder.add_conditional_edges("agent", tools_condition)

# Sau khi thực hiện tools xong thì quay lại Agent Node để đánh giá kết quả
builder.add_edge("tools", "agent")

# Biên dịch Graph
graph = builder.compile()

# 6. Chat loop
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✈️ TravelBuddy - Trợ lý Du lịch Thông minh ✈️")
    print(" Gõ 'quit', 'exit' hoặc 'q' để thoát")
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\nBạn: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ("quit", "exit", "q"):
                print("Cảm ơn bạn đã sử dụng TravelBuddy! Hẹn gặp lại.")
                break
                
            print("\nTravelBuddy đang suy nghĩ...")
            # Gọi Graph thực thi với input tin nhắn của user
            result = graph.invoke({"messages": [("human", user_input)]})
            
            # Lấy tin nhắn cuối cùng (là text từ Agent trả về)
            final = result["messages"][-1]
            print(f"\nTravelBuddy: {final.content}")
            print("-" * 60)
        except Exception as e:
            print(f"\n[Lỗi] Đã có lỗi xảy ra: {e}. Vui lòng thử lại.")
