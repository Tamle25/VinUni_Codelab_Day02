# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:
* 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
* 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = ____ phút/lượt**.
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Khách hàng   │     │ Cố vấn Dịch  │     │ Tra cứu Sổ   │     │ Nhập thông   │
│ gọi/nhắn mô  │ ──→ │ vụ (CVDV) hỏi│ ──→ │ tay Kỹ thuật │ ──→ │ tin & tạo    │
│ tả sự cố xe  │     │ lại chi tiết │     │ & Mã lỗi DTC │     │ Phiếu dịch vụ│
│ Ai: Khách    │     │ Ai: CVDV     │     │ Ai: CVDV     │     │ Ai: CVDV     │
│ ⏱ 3 phút     │    │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴 │     │ ⏱ 2 phút    │
│ In: Lời nói  │     │ In: Note tay │     │ In: Note     │     │ In: Thông tin│
│ Out: Raw text│     │ Out: Mô tả   │     │ Out: Mã lỗi  │     │ Out: Ticket  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Phân công    │
                                                               │ Kỹ thuật viên│
                                                               │ Ai: Quản xưởng│
                                                               │ ⏱ 2 phút     │
                                                               └──────────────┘
🔴 = Bottlenecks
⏱ Tổng thời gian xử lý thủ công: 17 phút/lượt tiếp nhận.

## 3.2. Problem Statement (6-field) & Metrics (15 min)
Điền đầy đủ 6 trường thông tin của bài toán:

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** |Cố vấn Dịch vụ (Service Advisor) tại các Xưởng Dịch Vụ VinFast toàn quốc. |
| **2. Current Workflow** | Khách hàng phản ánh hiện tượng bất thường của xe điện (VF5, VF8, VF9...) qua App/Hotline/Trực tiếp. Cố vấn dịch vụ phải ghi chép lại, hỏi đi hỏi lại để làm rõ, sau đó lật giở tài liệu kỹ thuật/Database mã lỗi (DTC) thủ công để xác định nhóm hệ thống bị lỗi (Pin/Truyền động/Khung gầm/Phần mềm/Điều hòa) và lập Phiếu dịch vụ. |
| **3. Bottleneck** | Bước 2 & 3 (mất 10 phút/lượt): Khách hàng dùng ngôn ngữ đời thường, từ tượng thanh (ví dụ: "xe bị giật khật khật khi nhấn ga", "màn hình bị treo đen thui", "sạc pin kêu o o"). Cố vấn dịch vụ mất nhiều thời gian hỏi lại và dịch từ ngôn ngữ dân dã sang từ vựng kỹ thuật chuẩn hóa để tra sổ tay. |
| **4. Business Impact** | Vào đợt bảo dưỡng ca cao điểm, mỗi Xưởng dịch vụ tiếp nhận >50 lượt xe/ngày. Tốn ~8.3 giờ làm việc/ngày của Cố vấn dịch vụ chỉ để tiếp nhận ban đầu. Gây ùn tắc tại xưởng, khách hàng chờ đợi lâu dẫn đến chỉ số hài lòng (CSAT) giảm 12%. |
| **5. Success Metric** |1. Giảm tổng thời gian tiếp nhận & phân loại lỗi từ 17 phút xuống dưới 3 phút/lượt (Efficiency).
2. Tỉ lệ AI trích xuất đúng nhóm hệ thống bị lỗi và gợi ý chính xác mã DTC ban đầu đạt >= 90% (Quality). |
| **6. Operational Boundary** |AI chỉ đóng vai trò Trợ lý đề xuất (Drafting & Suggesting). CẤM: AI tuyệt đối không được tự động xác nhận đặt lịch sửa chữa hay đưa ra kết luận bảo hành chính thức cho khách hàng mà không có Cố vấn dịch vụ kiểm duyệt (HITL). AI không được tự ý báo giá chi phí phụ tùng.|

## 3.3. Future-State Flow & AI Fit (25 min)
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [ ] Rule / State-Machine [ ] LLM Feature [ ] Agentic Loop.
* **Vẽ Future-State Flow:** Đánh dấu rõ:
  * 🔵 **AI Step:** Tác vụ LLM xử lý.
  * 🟢 **Human Step (HITL):** Bước con người phê duyệt/review (Human-in-the-loop).
  * ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.
AI Fit: Chọn LLM Feature (Structured Information Extraction & Classification). Không dùng Agent tự trị vì quy trình tiếp nhận dịch vụ yêu cầu tính chính xác cao, tuân thủ bảng mã lỗi DTC cố định của VinFast.
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Khách nhập/  │     │ 🔵 AI Extract│     │ 🔵 AI Draft  │     │ 🟢 CVDV      │
│ nói mô tả    │ ──→ │ & Classify   │ ──→ │ Phiếu Dịch   │ ──→ │ Check, Sửa   │
│ trên App/Web │     │ (Gemini LLM) │     │ vụ & Mã DTC  │     │ & Phê duyệt  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI không tự tin
                                                               (<70%), gắn tag 
                                                               "Cần Cố vấn kiểm
                                                               tra trực tiếp".
# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)
AI Readiness Checklist:
[x] Data Readiness: Đã có sẵn bộ từ điển mã lỗi DTC của VinFast và lịch sử log 10,000+ ticket tiếp nhận dịch vụ để làm dữ liệu Few-shot/Evaluation.

[x] Risk Control: Rủi ro nằm trong tầm kiểm soát 100% vì luôn có Cố vấn dịch vụ duyệt phiếu (HITL) trước khi gửi cho kỹ thuật viên hoặc khách hàng.

[x] Stakeholder Readiness: Ban Giám đốc Khối Dịch vụ Sau bán hàng VinFast rất ủng hộ vì giúp giảm áp lực cho Cố vấn Dịch vụ và tăng CSAT.

Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] GO (Bắt đầu xây dựng Prototype): Cho phép phát triển bản MVP triển khai thử nghiệm tại 2 Xưởng Dịch Vụ VinFast lớn nhất ở Hà Nội (Vincom Long Biên) và TP.HCM (Vincom Thảo Điền).

Justification (Lý giải quyết định):

Bài toán có tính khả thi kỹ thuật cực kỳ cao (sử dụng Gemini 2.5 Flash trích xuất thông tin cấu trúc), chi phí API thấp (~0.001$/lượt tiếp nhận), thời gian hoàn vốn (ROI) nhanh nhờ tiết kiệm >80% thời gian tiếp nhận ban đầu của Cố vấn dịch vụ. Ranh giới an toàn được bảo vệ chặt chẽ qua Prompt Boundary và mô hình Human-in-the-loop.