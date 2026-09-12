# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).


### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | VinFast| 1. Repetitive| So khớp và xử lý thủ công các giao dịch sạc điện bị lỗi, gián đoạn hoặc sai lệch tiền cọc.|
| 2 | Xanh SM|4. Stakeholder Pain | Gợi ý điểm nóng đón khách chưa chính xác khiến tài xế tốn pin chạy trống và tăng thời gian chờ.|
| 3 |Vinhomes |2. Time-consuming |BQL phân loại và soạn thảo thủ công phản hồi phản ánh/khiếu nại của cư dân trên App Resident. |
| 4 | Vinpearl| 3. AI-upgrade|Chatbot trả lời rập khuôn theo kịch bản, chưa thể tư vấn và thiết kế lịch trình combo phòng-vé cá nhân hóa. |
| 5 | Vinmec| 2. Time-consuming & 1. Repetitive|Bác sĩ mất nhiều thời gian nhập liệu và cấu trúc hóa ghi chú lâm sàng, hồ sơ khám bệnh vào hệ thống EMR. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: So khớp và xử lý thủ công các giao dịch sạc điện  │
│ bị lỗi, gián đoạn hoặc sai lệch tiền cọc tại trạm sạc.      │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau? Chủ xe điện / Tài xế (bị giữ cọc/treo giao dịch│
│ ), Nhân viên Vận hành Trạm sạc (tồn đọng ticket xử lý).    │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Khách hàng/Tài xế gửi ticket báo lỗi sạc/treo tiền    │
│   → 2. NVVH truy vấn dữ liệu telemetry trạm sạc để xác minh│
│   → 3. NVVH so sánh log giao dịch ngân hàng/ví với log trạm │
│   → 4. NVVH đối soát thủ công và tính toán số tiền chênh lệch│
│   → 5. Tạo lệnh hoàn tiền/điều chỉnh trên hệ thống kế toán  │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3-4 (⏱ 15–20 phút/ticket)         │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3-4            │
│ (Tự động đọc log telemetry + log giao dịch để phát hiện     │
│ bất thường và tự động đề xuất lệnh hoàn tiền/đối soát)      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian xử lý 1 ticket lỗi từ 20 phút ──> dưới 2 phút│
│ Giảm 80% số lượng ticket tồn đọng cần con người can thiệp. │
│                                                             │
│ Quick Architecture: [x] Agent (Anomaly Detection & Auto-Recon)│
└─────────────────────────────────────────────────────────────┘
```

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: BQL phân loại và soạn thảo thủ công phản hồi     │
│ phản ánh/khiếu nại của cư dân trên App Vinhomes Resident.   │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau? Ban quản lý KĐT (tốn thời gian soạn câu trả    │
│ lời), Cư dân (chờ đợi lâu, nhận phản hồi rập khuôn).        │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi phản ánh (tiếng ồn, vệ sinh, phí) qua App  │
│   → 2. Nhân viên CSKH đọc, phân loại nội dung và gán bộ phận│
│   → 3. CSKH tra cứu nội quy/quy trình KĐT tương ứng        │
│   → 4. CSKH gõ nháp phản hồi và bấm gửi cho cư dân          │
│                                                             │
│ Bước nào tốn nhất? Bước 3-4 (⏱ 10–12 phút/ý kiến)           │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3-4            │
│ (Phân loại tự động, RAG tra cứu nội quy KĐT và draft câu    │
│ trả lời chuẩn hóa cá nhân hóa cho nhân viên duyệt)          │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian phản hồi cư dân từ 12 tiếng ──> dưới 30 phút.│
│ Giảm thời gian soạn phản hồi của CSKH từ 10 phút ──> 2 phút. │
│                                                             │
│ Quick Architecture: [x] LLM Feature (RAG Copilot cho CSKH)  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Bác sĩ mất nhiều thời gian nhập liệu và cấu trúc  │
│ hóa ghi chú lâm sàng, hồ sơ khám bệnh vào hệ thống EMR.     │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau? Bác sĩ (quá tải hành chính), Bệnh nhân (thời   │
│ gian bác sĩ tương tác trực tiếp bị giảm).                   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bác sĩ hỏi bệnh và khám lâm sàng cho bệnh nhân        │
│   → 2. Bác sĩ viết tay hoặc gõ thô ghi chú chẩn đoán/kê đơn │
│   → 3. Bác sĩ chuẩn hóa dữ liệu theo mã ICD-10/mẫu EMR     │
│   → 4. Bác sĩ rà soát và lưu hồ sơ bệnh án điện tử          │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 15–20 phút/bệnh nhân)        │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3              │
│ (Chuyển giọng nói/ghi chú thô thành văn bản, tự động trích  │
│ xuất triệu chứng và gợi ý mã ICD-10 chuẩn hóa EMR)          │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian nhập liệu EMR từ 20 phút ──> dưới 5 phút/ca. │
│ Tăng thời gian bác sĩ tương tác trực tiếp với bệnh nhân 30%.│
│                                                             │
│ Quick Architecture: [x] LLM Feature (Medical Scribe & Structuring)│
└─────────────────────────────────────────────────────────────┘

```
Lý do chọn Card 1 (VinFast - Đối soát giao dịch sạc):Tác động trực tiếp đến dòng tiền & vận hành: Ảnh hưởng song song cả người dùng cá nhân lẫn toàn bộ đội xe Xanh SM. Dữ liệu (telemetry + log ngân hàng) có cấu trúc sẵn, hoàn toàn đo lường được ROI rõ ràng khi tự động hóa.Tính khả thi kỹ thuật cao: Phù hợp để xây dựng AI Agent / Anomaly Detection xử lý logic tự động, giải quyết triệt để bài toán lặp lại (Repetitive) cấp thiết.

Lý do không chọn Card 2 (Vinhomes - Phản hồi cư dân):Rủi ro sai sót thông tin liên quan đến phí quản lý, quy định KĐT hoặc tranh chấp pháp lý có thể dẫn đến khiếu nại nặng. Bài toán này giai đoạn đầu ưu tiên giải quyết bằng Rule-based router / template đơn giản hơn là cần tới AI phức tạp.

Lý do không chọn Card 3 (Vinmec - Cấu trúc hóa EMR y tế):Yêu cầu độ chính xác tuyệt đối ($>99.9\%$) về thuật ngữ chuyên ngành và mã y khoa ICD-10. Rào cản pháp lý/về tính riêng tư dữ liệu sức khỏe (HIPAA/GDPR) cao, chu kỳ thẩm định kỹ thuật và kiểm thử y khoa kéo dài.