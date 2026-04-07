# KẾT QUẢ TEST CAES - LAB 4

## Test 1 - Direct Answer (Không cần tool)
**User:** `Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.`

**Log Console & Trả lời:**
```text
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Chào bạn! Rất vui được hỗ trợ bạn trong việc lên kế hoạch chuyến đi. Bạn có thể cho mình biết thêm một chút về sở thích hoặc mục tiêu chuyến đi của bạn không? Bạn thích đi biển, núi, hay khám phá thành phố? Ngoài ra, nếu bạn đã có điểm đến nào trong đầu, hãy cho mình biết nhé!
```

## Test 2 - Single Tool Call
**User:** `Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng`

**Log Console & Trả lời:**
```text
[LOG] LLM quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}
[LOG] Kết quả trả về từ tool [search_flights]:
Danh sách chuyến bay từ Hà Nội đến Đà Nẵng:
- Vietnam Airlines: Khởi hành 06:00 - Đến 07:20, Giá: 1.450.000đ (economy)
- Vietnam Airlines: Khởi hành 14:00 - Đến 15:20, Giá: 2.800.000đ (business)
- VietJet Air: Khởi hành 08:30 - Đến 09:50, Giá: 890.000đ (economy)
- Bamboo Airways: Khởi hành 11:00 - Đến 12:20, Giá: 1.200.000đ (economy)
----------------------------------------
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Dưới đây là danh sách chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines**
   - Khởi hành: 06:00 - Đến: 07:20
   - Giá: 1.450.000đ (economy)

2. **Vietnam Airlines**
   - Khởi hành: 14:00 - Đến: 15:20
   - Giá: 2.800.000đ (business)

3. **VietJet Air**
   - Khởi hành: 08:30 - Đến: 09:50
   - Giá: 890.000đ (economy)

4. **Bamboo Airways**
   - Khởi hành: 11:00 - Đến: 12:20
   - Giá: 1.200.000đ (economy)

Nếu bạn cần thêm thông tin hoặc muốn đặt vé, hãy cho tôi biết nhé!
```

## Test 3 - Multi-Step Tool Chaining
**User:** `Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!`

**Log Console & Trả lời:**
```text
[LOG] LLM quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}
[LOG] Kết quả trả về từ tool [search_flights]:
Danh sách chuyến bay từ Hà Nội đến Phú Quốc:
- Vietnam Airlines: Khởi hành 07:00 - Đến 09:15, Giá: 2.100.000đ (economy)
- VietJet Air: Khởi hành 10:00 - Đến 12:15, Giá: 1.350.000đ (economy)
- VietJet Air: Khởi hành 16:00 - Đến 18:15, Giá: 1.100.000đ (economy)
----------------------------------------
[LOG] LLM quyết định gọi tool: calculate_budget với tham số {'total_budget': 5000000, 'expenses': 'vé_máy_bay:1350000'}
[LOG] Kết quả trả về từ tool [calculate_budget]:
Bảng chi phí:
- vé_máy_bay: 1.350.000đ
---
Tổng chi: 1.350.000đ
Ngân sách: 5.000.000đ
Còn lại: 3.650.000đ
----------------------------------------
[LOG] LLM quyết định gọi tool: search_hotels với tham số {'city': 'Phú Quốc', 'max_price_per_night': 1825000}
[LOG] Kết quả trả về từ tool [search_hotels]:
Danh sách khách sạn tại Phú Quốc (Giá <= 1.825.000đ/đêm):
- 9Station Hostel (2 sao, Khu: Dương Đông) | Rating: 4.5 | Giá: 200.000đ/đêm
- Sol by Meliá (4 sao, Khu: Bãi Trường) | Rating: 4.2 | Giá: 1.500.000đ/đêm
- Lahana Resort (3 sao, Khu: Dương Đông) | Rating: 4.0 | Giá: 800.000đ/đêm
----------------------------------------
[LOG] LLM quyết định gọi tool: calculate_budget với tham số {'total_budget': 5000000, 'expenses': 'vé_máy_bay:1350000,khách_sạn:3000000'}
[LOG] Kết quả trả về từ tool [calculate_budget]:
Bảng chi phí:
- vé_máy_bay: 1.350.000đ
- khách_sạn: 3.000.000đ
---
Tổng chi: 4.350.000đ
Ngân sách: 5.000.000đ
Còn lại: 650.000đ
----------------------------------------
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: ### Kế hoạch chuyến đi
**Chuyến bay:** 
- **Hãng:** VietJet Air
- **Giờ:** Khởi hành 10:00 - Đến 12:15
- **Giá:** 1.350.000đ

**Khách sạn:**
- **Tên:** Sol by Meliá
- **Đánh giá:** 4.2 sao
- **Giá:** 1.500.000đ/đêm (tổng cho 2 đêm là 3.000.000đ)

**Ngân sách:**
- **Tổng chi phí:** 4.350.000đ
- **Tiền dư:** 650.000đ

**Gợi ý:** 
- Bạn có thể sử dụng số tiền dư để thưởng thức những món ăn đặc sản hoặc tham gia một số hoạt động giải trí tại Phú Quốc. Chúc bạn có một chuyến đi tuyệt vời!
```

## Test 4 - Missing Info / Clarification
**User:** `Tôi muốn đặt khách sạn`

**Log Console & Trả lời:**
```text
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Bạn muốn đặt khách sạn ở thành phố nào và có ngân sách tối đa mỗi đêm là bao nhiêu?
```

## Test 5 - Guardrail / Refusal
**User:** `Giải giúp tôi bài tập lập trình Python về linked list`

**Log Console & Trả lời:**
```text
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Xin lỗi, nhưng mình không thể giúp bạn với các bài tập lập trình hoặc lập trình cụ thể. Tuy nhiên, mình có thể tư vấn về các chuyến đi hoặc các hoạt động du lịch tại Việt Nam nếu bạn cần. Bạn có muốn lên kế hoạch cho một chuyến đi không?
```

