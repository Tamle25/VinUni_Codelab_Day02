# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **VinFast** | Chẩn đoán lỗi xe từ mô tả tiếng Việt của khách | AI có thể tốt hơn | Khách hàng mô tả tiếng Việt (ví dụ: *"xe đi qua gờ giảm tốc kêu cụp cụp ở bánh trước"*), hệ thống tự động phân loại mã lỗi kỹ thuật ban đầu |
| 2 | **VinFast** | Lặp lại  | So khớp hóa đơn sạc điện đối tác: Tự động đối chiếu dữ liệu sạc hằng tuần từ hàng nghìn trụ sạc liên kết ngoài với bảng kê chi tiết hóa đơn thực tế gửi về phòng tài chính kế toán |
| 3 | **Vinhomes** | Tốn thời gian | Phân loại & Route tự động phản ánh cư dân: Hệ thống tự động đọc, phân loại mức độ khẩn cấp và chuyển giao (route) chính xác các phản ánh/khiếu nại gửi qua App Vinhomes Resident đến đúng Ban quản lý tòa nhà |
| 4 | **Vinmec** | Pain từ người khác | Tóm tắt hồ sơ xuất viện (Discharge Summary): Trích xuất dữ liệu lâm sàng, kết quả xét nghiệm và ghi chú của bác sĩ để tự động tạo bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân, giúp bác sĩ giảm tải thủ tục hành chính |
| 5 | | | |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tự động chẩn đoán và phân loại mã lỗi kỹ thuật    │
│ ban đầu từ mô tả tự do bằng tiếng Việt của khách hàng VinFast│
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                                                             │
│ Ai đang đau? Cố vấn dịch vụ (quá tải khi tiếp nhận) và      │
│ Khách hàng (chờ đợi xếp lịch lâu, diễn tả lỗi khó khăn).    │
│                                                             │
│ Workflow thủ công hiện hiện tại (5 bước):                   │
│   1. Khách hàng gọi/nhắn tin mô tả hiện tượng lạ trên xe    │
│   ──> 2. Cố vấn dịch vụ nghe/đọc và hỏi thêm thông tin      │
│   ──> 3. Tra cứu thủ công Sổ tay Kỹ thuật / Mã lỗi DTC      │
│   ──> 4. Nhập thông tin vào hệ thống quản lý xưởng dịch vụ  │
│   ──> 5. Xếp lịch hẹn và gán KTV chuyên trách thích hợp     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 15 phút/lượt) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3-4            │
│ (Trích xuất triệu chứng -> Chuẩn hóa DTC -> Draft phiếu hẹn)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian tiếp nhận & phân loại lỗi từ 15 min ──> 2 min│
│ Độ chính xác phân loại nhóm hệ thống lỗi đạt >= 90%.        │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Trích xuất & Phân loại)│
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #4                                       │
│                                                             │
│ Bài toán: Trích xuất bệnh án điện tử để soạn thảo tóm tắt   │
│ hồ sơ xuất viện (Discharge Summary) ngôn ngữ dễ hiểu.       │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinmec    │
│                                                             │
│ Ai đang đau? Bác sĩ (tốn 20-30p write-up thủ công) và       │
│ Bệnh nhân (khó hiểu các thuật ngữ y khoa phức tạp).         │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bác sĩ mở Hồ sơ bệnh án điện tử (EMR)                  │
│   ──> 2. Tổng hợp kết quả xét nghiệm, đơn thuốc, ghi chú   │
│   ──> 3. Tự gõ bản Tóm tắt xuất viện và dặn dò tái khám    │
│   ──> 4. In ấn và giải thích cho bệnh nhân                  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 25 phút/ca)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3               │
│ (Trích xuất dữ liệu EMR -> Draft bản tóm tắt chuẩn định dạng)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian soạn hồ sơ từ 25 phút ──> dưới 3 phút/bệnh nhân│
│ 100% hồ sơ bắt buộc có Bác sĩ kiểm duyệt (HITL).            │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Summarization & Draft) │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Phân loại mức độ ưu tiên và tự động route phản    │
│ ánh của cư dân trên App Vinhomes Resident đến đúng BQL Tòa  │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                                                             │
│ Ai đang đau? Cư dân (chờ phản hồi lâu) & Ban Quản lý (BQL)   │
│ (mất thời gian đọc, lọc và chuyển tiếp thủ công).           │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh lên App Vinhomes Resident          │
│   ──> 2. Nhân viên CSKH Trung tâm đọc và phân loại thủ công │
│   ──> 3. Chuyển tiếp (Route) ticket tới BQL Tòa nhà tương ứng│
│   ──> 4. BQL Tòa nhà nhận ticket và giao kỹ thuật xử lý    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ 30 phút/ticket) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3               │
│ (Đọc văn bản -> Phân loại mức độ P1-P4 -> Auto-route ticket)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian routing ticket từ 30 phút ──> dưới 10 giây.   │
│ Tỉ lệ phân loại đúng bộ phận đạt >= 95%.                    │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Classification Router)  │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---
