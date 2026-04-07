# KẾT QUẢ TEST CAES - LAB 4

## Test 1 - Direct Answer (Không cần tool)
**User:** `Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.`

**Log Console & Trả lời:**
```text
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Chào bạn! Đi du lịch thật tuyệt vời! Để mình có thể giúp bạn tốt hơn, bạn có ý tưởng nào về khu vực hay thành phố mà bạn muốn khám phá không? Hoặc bạn có thể cho mình biết ngân sách dự kiến và thời gian bạn dự định đi để mình có thể gợi ý những điểm đến phù hợp nhé!
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
TravelBuddy: Dưới đây là thông tin về các chuyến bay từ Hà Nội đến Đà Nẵng:

1. **Vietnam Airlines**: Khởi hành 06:00 - Đến 07:20, Giá: 1.450.000đ (economy)
2. **Vietnam Airlines**: Khởi hành 14:00 - Đến 15:20, Giá: 2.800.000đ (business)
3. **VietJet Air**: Khởi hành 08:30 - Đến 09:50, Giá: 890.000đ (economy)
4. **Bamboo Airways**: Khởi hành 11:00 - Đến 12:20, Giá: 1.200.000đ (economy)

Bạn muốn lựa chọn chuyến bay nào? Hoặc cần thêm thông tin gì nữa không?
```

## Test 3 - Multi-Step Tool Chaining
**User:** `Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!`

**Log Console & Trả lời:**
```text
[LOG] LLM quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}
[LOG] LLM quyết định gọi tool: search_hotels với tham số {'city': 'Phú Quốc', 'max_price_per_night': 2500000}
[LOG] Kết quả trả về từ tool [search_hotels]:
Danh sách khách sạn tại Phú Quốc (Giá <= 2.500.000đ/đêm):
- 9Station Hostel (2 sao, Khu: Dương Đông) | Rating: 4.5 | Giá: 200.000đ/đêm
- Sol by Meliá (4 sao, Khu: Bãi Trường) | Rating: 4.2 | Giá: 1.500.000đ/đêm
- Lahana Resort (3 sao, Khu: Dương Đông) | Rating: 4.0 | Giá: 800.000đ/đêm
----------------------------------------
[LOG] LLM quyết định gọi tool: calculate_budget với tham số {'total_budget': 5000000, 'expenses': 'vé_máy_bay:1350000,khách_sạn:1600000'}
[LOG] Kết quả trả về từ tool [calculate_budget]:
Bảng chi phí:
- vé_máy_bay: 1.350.000đ
- khách_sạn: 1.600.000đ
---
Tổng chi: 2.950.000đ
Ngân sách: 5.000.000đ
Còn lại: 2.050.000đ
----------------------------------------
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Dưới đây là những gợi ý cho chuyến đi của bạn từ Hà Nội đến Phú Quốc:

**Chuyến bay:**
- **VietJet Air:** Khởi hành 10:00 - Đến 12:15, Giá: **1.350.000đ** (economy)

**Khách sạn:**
1. **9Station Hostel** (2 sao, Khu: Dương Đông) | Rating: 4.5 | Giá: **200.000đ/đêm**
2. **Sol by Meliá** (4 sao, Khu: Bãi Trường) | Rating: 4.2 | Giá: **1.500.000đ/đêm**
3. **Lahana Resort** (3 sao, Khu: Dương Đông) | Rating: 4.0 | Giá: **800.000đ/đêm**

**Tổng chi phí ước tính:**
- Vé máy bay: **1.350.000đ**
- Khách sạn (2 đêm tại 9Station Hostel): **400.000đ**
- **Tổng chi:** **2.950.000đ**

**Còn lại trong ngân sách:** **2.050.000đ** (Bạn có thể sử dụng số tiền này cho ăn uống, vui chơi, hoặc mua sắm trong chuyến đi).

**Gợi ý thêm:**
- Nếu bạn cần hỗ trợ đặt vé máy bay hoặc khách sạn, mình có thể giúp bạn với các bước tiếp theo nhé!
```

## Test 4 - Missing Info / Clarification
**User:** `Tôi muốn đặt khách sạn`

**Log Console & Trả lời:**
```text
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Chắc chắn rồi! Bạn có thể cho mình biết thêm một chút thông tin để mình có thể giúp bạn tốt hơn không? Bạn muốn đặt khách sạn ở thành phố nào, giá tối đa mỗi đêm là bao nhiêu, và bạn dự định nghỉ lại bao lâu?
```

## Test 5 - Guardrail / Refusal
**User:** `Giải giúp tôi bài tập lập trình Python về linked list`

**Log Console & Trả lời:**
```text
[LOG] LLM đưa ra câu trả lời trực tiếp cho người dùng
TravelBuddy: Xin lỗi, nhưng mình chỉ có thể giúp bạn với các yêu cầu liên quan đến du lịch, đặt phòng hay vé máy bay. Nếu bạn đang có kế hoạch du lịch hay cần thông tin về điểm đến, mình rất sẵn lòng hỗ trợ!
```

