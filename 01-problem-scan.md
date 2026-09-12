# 01 — Problem Scan & Quick Cards (Vin Smart Future)

**Tác giả:** Lương (Nhánh cá nhân: `Luong02932`)  
**Đơn vị:** Vin Smart Future — Khối Công nghệ Vingroup  
**Dự án:** Trợ lý AI Điều phối Thông minh Xanh SM (GSM)

---

## 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (4 Lenses)

Áp dụng 4 Lenses (Lặp lại, Tốn thời gian, AI có thể tốt hơn, Pain từ người khác) để quét qua các hoạt động vận hành của các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM** | Lặp lại | So khớp và phân bổ lại cuốc xe khi khách hàng yêu cầu thay đổi điểm đến giữa chừng. |
| 2 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế về sự cố sạc pin hoặc va chạm thực địa (mất 15-20 min/lượt). |
| 3 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện và đối chiếu số liệu trạm sạc đối tác hằng tuần. |
| 4 | **Vinhomes** | AI-upgrade | Hệ thống phân loại và route tự động các phản hồi/khiếu nại của cư dân trên App Vinhomes Resident (CSKH phản hồi rập khuôn, mất 12 tiếng). |
| 5 | **Vinmec** | Pain từ người khác | Bác sĩ mất quá nhiều thời gian viết tóm tắt hồ sơ xuất viện (mất 20-30 phút/bệnh nhân, bác sĩ phàn nàn vì quá tải). |
| 6 | **Xanh SM** | Tốn thời gian | Tóm tắt lý do khách hàng hủy chuyến từ cuộc gọi ghi âm và ghi chú của tài xế để tìm pattern lỗi hệ thống. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Chọn top 3 bài toán tiềm năng nhất từ bảng SCAN: **Card #2 (Xanh SM Sự cố sạc), Card #4 (Vinhomes CSKH), Card #6 (Xanh SM Hủy chuyến).**

### Quick Problem Card #1: Xanh SM Xử lý sự cố sạc pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 (Ưu tiên số 1)                        │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo cáo sự cố sạc pin / hết pin    │
│ giữa đường cần điều phối cứu hộ hoặc trạm sạc gần nhất.     │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (chờ đợi), Điều phối viên (quá tải)     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo hết pin               │
│   → 2. Điều phối viên tra cứu thủ công vị trí xe trên bản đồ│
│   → 3. Tra cứu thủ công các trạm sạc VinFast còn trụ trống   │
│   → 4. Viết tin nhắn chỉ dẫn/đường đi gửi qua App tài xế    │
│   → 5. Liên hệ đội xe cứu hộ nếu xe đã cạn kiệt pin (< 5%)   │
│                                                             │
│ Bước nào tốn nhất? Bước 3-4 (⏱ 10-12 phút/lượt)              │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4              │
│ (Tự động hóa lấy vị trí -> Tra cứu trạm trống -> Draft tin) │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.      │
│ Tỉ lệ chỉ dẫn trạm sạc chính xác đạt >= 98%.                │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Tự động soạn chỉ dẫn)   │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #2: Vinhomes Phân loại và Điều phối Phản hồi Cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Cư dân gửi khiếu nại/yêu cầu qua Vinhomes Resident│
│ App bị nghẽn ở khâu phân loại bộ phận xử lý (kỹ thuật, an   │
│ ninh, vệ sinh, kế toán).                                    │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Cư dân (chờ đợi lâu), Ban Quản lý (quá tải vé) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi ticket khiếu nại qua App                    │
│   → 2. Lễ tân đọc thủ công từng ticket                      │
│   → 3. Chọn bộ phận xử lý và forward phiếu                  │
│   → 4. Soạn tin nhắn phản hồi đã tiếp nhận cho cư dân       │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 10 phút/ticket, tích tụ 12h)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Phân loại văn bản tự động + trích xuất độ khẩn cấp)        │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian điều phối ticket từ 12 giờ xuống dưới 15 phút│
│ Độ chính xác gán nhãn phân loại đạt >= 95%.                 │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Text Classification)   │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #3: Xanh SM Phân tích Nguyên nhân Hủy chuyến

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Tóm tắt và phân tích nguyên nhân gốc rễ khách hàng │
│ hủy chuyến từ hội thoại tổng đài và note tài xế.            │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Bộ phận Vận hành (không nắm được pattern lỗi)  │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Xuất file log các cuốc xe bị hủy cuối ngày             │
│   → 2. Nghe mẫu ghi âm cuộc gọi và đọc ghi chú              │
│   → 3. Nhập tay lý do vào bảng tính Excel                   │
│   → 4. Làm báo cáo tuần tổng kết tỉ lệ hủy                  │
│                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 3-4 giờ/ngày của chuyên viên│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3            │
│ (Trích xuất nguyên nhân từ text & speech-to-text tự động)   │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Tự động hóa 100% khâu gắn thẻ lý do hủy chuyến trong ngày   │
│ Cung cấp báo cáo dashboard nguyên nhân hủy theo thời gian   │
│ thực (thay vì trễ 1 tuần).                                  │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Offline Summarization) │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Quyết định lựa chọn: Card #1 (Xanh SM Sự cố sạc pin)

- **Lý do chọn Card #1:** Ảnh hưởng trực tiếp đến an toàn vận hành thời gian thực (real-time) của tài xế và trải nghiệm khách hàng của Xanh SM. Thời gian xử lý thủ công (15 phút) gây tắc nghẽn nghiêm trọng vào giờ cao điểm.
- **Ranh giới an toàn rõ ràng:** Có thể áp dụng kiểm duyệt con người (Human-in-the-Loop) với thẻ `[DRAFT_ONLY]` và ngưỡng pin `< 5%` để điều xe sạc di động (Mobile Charger), hạn chế tối đa rủi ro chết máy giữa đường.
