# Phase 1 & 2 Deliverable — Problem Scan & Quick Cards (Vin Smart Future)

**Họ và tên:** AI Product Engineer  
**Đơn vị:** Vin Smart Future (Vingroup)  
**Ngày thực hiện:** 2026-09-12  

---

## 🔍 Phase 1 — SCAN: Danh sách bài toán vận hành Vingroup

Sử dụng **4 Lenses** (*Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác*) quét qua hoạt động của các công ty thành viên Vingroup:

| # | Công ty thành viên | Lens | Mô tả ngắn bài toán / Bottleneck vận hành |
|---|--------------------|------|-------------------------------------------|
| 1 | **Xanh SM (GSM)** | Tốn thời gian | Điều phối viên tra cứu thủ công vị trí xe và trạm sạc VinFast trống khi tài xế báo sự cố sạc/hết pin thực địa (mất 12-15 phút/lượt). |
| 2 | **VinFast** | Lặp lại | So khớp dữ liệu sạc điện từ các trạm sạc đối tác ngoài với hóa đơn thanh toán hàng tuần (xử lý hàng nghìn dòng dữ liệu thủ công). |
| 3 | **Vinhomes** | AI-upgrade | Phân loại tự động & định hướng khiếu nại cư dân trên App Vinhomes Resident (hiện tại CSKH phản hồi thủ công, chậm 8-12 tiếng). |
| 4 | **Vinpearl** | Pain từ người khác | Tự động quét review từ Booking/Agoda/Google Maps để phát hiện các phàn nàn dịch vụ khẩn cấp (phòng bẩn, thái độ NV) gửi Manager. |
| 5 | **Vinmec** | Tốn thời gian | Trích xuất thông tin bệnh án điện tử để draft Tóm tắt hồ sơ xuất viện (Discharge Summary) bằng ngôn ngữ dễ hiểu (bác sĩ mất 25 phút/bệnh nhân). |
| 6 | **Xanh SM (GSM)** | Pain từ người khác | Tổng hợp & phân loại nguyên nhân hủy chuyến từ cuộc gọi ghi âm tổng đài để tìm pattern lỗi điều xe. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

### 💳 QUICK PROBLEM CARD #1 — Xanh SM: Xử lý sự cố pin & điều phối cứu hộ thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo sự cố cạn pin/sạc pin khẩn    │
│ cấp cần chỉ dẫn trạm sạc trống hoặc điều xe cứu hộ di động. │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (chờ lâu), Dispatcher (quá tải) │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo sự cố pin              │
│   → 2. Dispatcher tra cứu định vị GPS xe trên bản đồ        │
│   → 3. Tra cứu trạm sạc VinFast trống phù hợp loại cổng sạc  │
│   → 4. Soạn thảo tin nhắn hướng dẫn/toạ độ gửi App tài xế   │
│   → 5. Liên hệ xe cứu hộ sạc di động nếu pin < 5%           │
│                                                             │
│ Bước nào tốn thời gian nhất? Bước 3 & 4 (⏱ 10 phút/lượt)     │
│ AI nhảy vào bước nào? Bước 3 & 4 (Auto-pull GPS -> Draft SMS)│
│                                                             │
│ Đo thành công bằng gì (Metric)?                              │
│ Giảm thời gian xử lý sự cố từ 15 min ──> dưới 3 min/lượt.   │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Vấn đề có cấu trúc)    │
└─────────────────────────────────────────────────────────────┘
```

---

### 💳 QUICK PROBLEM CARD #2 — Vinhomes: Trợ lý phân loại & phản hồi khiếu nại cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Phân loại tự động và draft phản hồi khiếu nại     │
│ của cư dân gửi qua App Vinhomes Resident đến đúng BQL.      │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau (Actor)? Cư dân (chờ lâu), Ban Quản Lý (quá tải) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh lên ứng dụng Vinhomes Resident     │
│   → 2. Lễ tân tòa nhà đọc văn bản, phân loại thủ công       │
│   → 3. Chuyển tiếp ticket tới kỹ thuật/vệ sinh/an ninh      │
│   → 4. Soạn thư xác nhận và hẹn thời gian xử lý             │
│                                                             │
│ Bước nào tốn thời gian nhất? Bước 2 & 4 (⏱ 15-30 phút/ticket) │
│ AI nhảy vào bước nào? Bước 2 & 4 (Auto-categorize & Draft)  │
│                                                             │
│ Đo thành công bằng gì (Metric)?                              │
│ Giảm thời gian phản hồi ban đầu từ 8 tiếng ──> dưới 15 phút.│
│                                                             │
│ Quick Architecture: [x] LLM Feature                         │
└─────────────────────────────────────────────────────────────┘
```

---

### 💳 QUICK PROBLEM CARD #3 — Vinmec: Tự động hóa tóm tắt hồ sơ xuất viện (Discharge Summary)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Trích xuất thông tin bệnh án điện tử (EMR) để     │
│ draft tóm tắt hồ sơ xuất viện chuẩn y khoa & dễ hiểu.       │
│ Công ty thành viên: [x] Vinmec                              │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ điều trị (quá tải thủ tục)      │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bác sĩ mở hệ thống EMR đọc lại lịch sử điều trị        │
│   → 2. Tổng hợp các kết quả xét nghiệm, đơn thuốc, chẩn đoán│
│   → 3. Gõ tay bản tóm tắt xuất viện bằng thuật ngữ y khoa   │
│   → 4. Giải thích lại cho bệnh nhân / người nhà             │
│                                                             │
│ Bước nào tốn thời gian nhất? Bước 2 & 3 (⏱ 25 phút/bệnh nhân)│
│ AI nhảy vào bước nào? Bước 2 & 3 (Auto EMR extract & Draft) │
│                                                             │
│ Đo thành công bằng gì (Metric)?                              │
│ Giảm thời gian chuẩn bị hồ sơ từ 25 min ──> 5 min (Bác sĩ  │
│ kiểm tra và ký phê duyệt).                                  │
│                                                             │
│ Quick Architecture: [x] LLM Feature với strict HITL         │
└─────────────────────────────────────────────────────────────┘
```
