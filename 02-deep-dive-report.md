# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:
* 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
* 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = ____ phút/lượt**.

┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Tiếp nhận    │     │ Tra cứu Log  │     │ Đối chiếu Log│     │ Tính toán &  │
│ Ticket lỗi   │ ──→ │ Telemetry    │ ──→ │ Thanh toán   │ ──→ │ Đề xuất hoàn │
│ sạc / cọc    │     │ trụ sạc      │     │ ngân hàng    │     │ tiền         │
│ Ai: CSKH     │     │ Ai: NVVH     │     │ Ai: NVVH     │     │ Ai: NVVH     │
│ ⏱ 5 phút     │     │ ⏱ 8 phút 🔴  │     │ ⏱ 7 phút 🔴  │     │ ⏱ 5 phút     │
│ In: App/Call │     │ In: ID Trụ   │     │ In: Mã GD    │     │ In: Số liệu  │
│ Out: Ticket  │     │ Out: Raw Log │     │ Out: Bank Log│     │ Out: Đề xuất │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
 🔄 Handoff 1          🔄 Handoff 2                             │
 (CSKH ──→ NVVH)       (Trạm ──→ Bank)                                │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Phê duyệt &  │
                                                               │ Thao tác hoàn│
                                                               │ tiền         │
                                                               │ Ai: Kế toán  │
                                                               │ ⏱ 5 phút 🔴  │
                                                               │ In: Đề xuất  │
                                                               │ Out: Lệnh tiền│
                                                               └──────────────┘
                                                                 🔄 Handoff 3
                                                                 (NVVH ──→ KTV)

🔴 Bottlenecks: Bước 2, Bước 3, Bước 5.
🔄 Handoffs: 
  • Handoff 1: CSKH ──> NVVH Trạm sạc (chuyển giao ticket).
  • Handoff 2: Dashboard VinFast ──> Portal Ngân hàng/Ví (chuyển ngữ cảnh tra cứu).
  • Handoff 3: NVVH Trạm sạc ──> Kế toán (gửi phê duyệt tài chính).

⏱ Tổng thời gian xử lý thủ công: 30 phút/lượt.



## 3.2. Problem Statement (6-field) & Metrics (15 min)
Điền đầy đủ 6 trường thông tin của bài toán:

| **1. Actor / Operator** | **Nhân viên Vận hành Trạm sạc (NVVH)** và **Chuyên viên Kế toán Đối soát** VinFast. |
| **2. Current Workflow** | NVVH nhận ticket báo lỗi sạc/treo cọc ──> Truy vấn thủ công log telemetry trụ sạc trên Dashboard VinFast ──> Đăng nhập Portal Ngân hàng/Ví điện tử đối chiếu giao dịch bằng Excel ──> Tính toán tiền chênh lệch ──> Gửi đề xuất phê duyệt sang Kế toán thực hiện lệnh hoàn tiền thủ công. |
| **3. Bottleneck** | **Bước 2, 3 và 5:** Bị tắc nghẽn ở việc tra cứu log telemetry phân tán, đối soát thủ công từng dòng giao dịch ngân hàng mất thời gian, và quy trình chuyển giao phê duyệt hoàn tiền qua nhiều khâu. |
| **4. Business Impact** | Tốn **30 phút/ticket** xử lý thủ công; thời gian hoàn tiền cho khách kéo dài **24–48 giờ** gây bức xúc; tiêu tốn hàng nghìn giờ làm việc/tháng của đội ngũ back-office và làm giảm chỉ số hài lòng (NPS) của chủ xe điện VinFast / tài xế Xanh SM. |
| **5. Success Metric** | Tự động hóa đối soát **>85%** số lượng ticket giao dịch lỗi; giảm thời gian xử lý 1 ticket từ **30 phút ──> dưới 2 phút**; rút ngắn SLA hoàn tiền cho khách từ **48 giờ ──> dưới 15 phút**. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Tự động thu thập log telemetry, trích xuất dữ liệu giao dịch ngân hàng, phát hiện bất thường, tính toán số tiền chênh lệch và tự động duyệt/hoàn tiền với các giao dịch giá trị nhỏ ($\le 200.000$ VNĐ). **TUYỆT ĐỐI KHÔNG ĐƯỢC:** Tự động chuyển tiền đối với các tài khoản có dấu hiệu gian lận/bất thường hoặc giao dịch $> 200.000$ VNĐ.**ĐIỂM CẦN DUYỆT (Human-in-the-loop):** Kế toán phải xem và bấm duyệt 1-click đối với các giao dịch vượt ngưỡng giá trị quy định hoặc hệ thống báo cờ rủi ro (flagged). |

## 3.3. Future-State Flow & AI Fit (25 min)
AI Fit: Chọn Agentic Loop (kết hợp Rule-based Anomaly Engine + LLM Decision Agent để vừa đảm bảo tính chính xác tuyệt đối của số liệu tài chính, vừa tự động hóa thao tác đối soát và ra quyết định xử lý).

Quy trình tương lai:

┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Tiếp nhận    │     │ 🔵 Auto-fetch│     │ 🔵 Anomaly    │     │ 🔵 Decision  │
│ Ticket lỗi   │ ──→ │ Telemetry &  │ ──→ │ Detection    │ ──→ │ Engine & Auto│
│ sạc / cọc    │     │ Payment Log  │     │ Reconciliation│    │ Resolution   │
│ Ai: System   │     │ Ai: AI Agent │     │ Ai: AI Agent │     │ Ai: AI Agent │
│ ⏱ 5 giây     │     │ ⏱ 10 giây    │     │ ⏱ 15 giây    │     │ ⏱ 10 giây    │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                   ┌──────────────────┴──────────────────┐
                                                   │                                     │
                                       (Đủ điều kiện ≤ 200k &            (Độ tự tin thấp /
                                        Độ tự tin High > 95%)             Sai lệch > 200k)
                                                   │                                     │
                                                   ▼                                     ▼
                                            ┌──────────────┐                      ┌──────────────┐
                                            │ Bước 5a      │                      │ 🟢 Bước 5b   │
                                            │ Tự động hoàn │                      │ Kế toán      │
                                            │ tiền & gửi   │                      │ click duyệt  │
                                            │ thông báo    │                      │ 1-click      │
                                            │ Ai: System   │                      │ Ai: Kế toán  │
                                            │ ⏱ 5 giây     │                      │ ⏱ 1-2 phút   │
                                            └──────────────┘                      └──────────────┘
                                                                                         │
                                                                                         │
                                                                                         ▼
                                                                                  ↩️ Fallback:
                                                                                  Nếu API lỗi hoặc
                                                                                  thiếu dữ liệu,
                                                                                  chuyển NVVH đối
                                                                                  soát thủ công
                                                                                  như quy trình cũ.


🔵 AI Step: Tác vụ AI Agent tự động xử lý.

🟢 Human Step (HITL): Kế toán phê duyệt/review 1-click dựa trên gợi ý của AI.

↩️ Fallback: Kế hoạch dự phòng chuyển về quy trình thủ công khi gặp lỗi dữ liệu/API.


# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [ ] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [ ] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[ ] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> *Viết lý giải chi tiết tại đây*
