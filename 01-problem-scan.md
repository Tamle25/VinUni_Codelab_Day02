# 01 — Problem Scan & Quick Assess
## Lab 02: AI Product Scoping — Vin Smart Future

> **Lưu ý:** Các con số về thời gian/tần suất bên dưới là giả định phục vụ scoping trong Lab, cần được xác minh bằng dữ liệu vận hành thực tế trước khi triển khai production.

---

# Phase 1 — SCAN

## Bảng quét cơ hội AI

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian / Stakeholder Pain | Điều phối viên phải tra vị trí xe, mức pin và trạm sạc phù hợp khi tài xế báo pin thấp; sau đó tự soạn hướng dẫn hoặc gọi cứu hộ. |
| 2 | VinFast | AI-upgrade | Hỗ trợ kỹ thuật phải đọc mô tả lỗi xe bằng tiếng Việt tự do để phân loại nhóm lỗi và chuyển đúng kỹ thuật viên. |
| 3 | Vinhomes | Lặp lại | Phản ánh cư dân từ ứng dụng phải được đọc, phân loại và chuyển thủ công đến đúng ban quản lý/tổ kỹ thuật. |
| 4 | Vinpearl | Tốn thời gian | Email đặt phòng theo đoàn có nhiều yêu cầu tự do; nhân viên phải đọc, trích xuất ngày, số phòng, loại phòng và yêu cầu đặc biệt. |
| 5 | Vinmec | Tốn thời gian / AI-upgrade | Bác sĩ/điều dưỡng phải tổng hợp nhiều nguồn thông tin để soạn bản tóm tắt xuất viện dễ hiểu cho bệnh nhân. |

---

# Phase 2 — QUICK-ASSESS

## Quick Problem Card #1 — Xanh SM: Điều phối sự cố pin thấp

**Bài toán:** Khi tài xế Xanh SM báo pin thấp/hết pin giữa đường, điều phối viên mất nhiều thời gian để kiểm tra vị trí, mức pin, trạm sạc phù hợp và soạn hướng dẫn xử lý.

**Công ty thành viên:** Xanh SM (GSM)

**Actor:** Điều phối viên trung tâm điều vận; tài xế là stakeholder bị ảnh hưởng trực tiếp.

### Workflow thủ công hiện tại

1. Tài xế báo sự cố pin qua tổng đài/app.
2. Điều phối viên xác nhận biển số, vị trí GPS và mức pin.
3. Điều phối viên tra cứu trạm sạc phù hợp và khoảng cách.
4. Điều phối viên soạn hướng dẫn cho tài xế.
5. Nếu pin quá thấp, điều phối viên liên hệ phương án cứu hộ/sạc di động.

**Bottleneck:** Bước 3–4, ước tính 8–10 phút/lượt.

**AI có thể hỗ trợ:** Tổng hợp dữ liệu đầu vào, chọn phương án theo rule an toàn, draft hướng dẫn cho dispatcher duyệt.

**Success Metric:**

- Giảm thời gian xử lý trung bình từ khoảng 15 phút xuống dưới 3 phút/lượt.
- 100% trường hợp pin < 5% không được hướng dẫn tới trạm > 5 km.
- 100% tin nhắn cho tài xế phải ở trạng thái `[DRAFT_ONLY]` trước khi con người duyệt.

**Quick Architecture:** Rule + LLM Feature.

---

## Quick Problem Card #2 — Vinhomes: Phân loại phản ánh cư dân

**Bài toán:** Phản ánh cư dân bằng ngôn ngữ tự do mất thời gian để nhân viên đọc, phân loại và chuyển tới đúng bộ phận xử lý.

**Công ty thành viên:** Vinhomes

**Actor:** Nhân viên chăm sóc cư dân/Ban quản lý tòa nhà.

### Workflow thủ công hiện tại

1. Cư dân gửi phản ánh trên app.
2. Nhân viên đọc nội dung.
3. Xác định nhóm vấn đề: điện, nước, an ninh, vệ sinh, tiếng ồn...
4. Chọn đơn vị xử lý phù hợp.
5. Gửi ticket và phản hồi ban đầu cho cư dân.

**Bottleneck:** Bước 2–4, ước tính 4–6 phút/ticket.

**AI có thể hỗ trợ:** Phân loại intent, trích xuất thông tin quan trọng, đề xuất routing và draft phản hồi ban đầu.

**Success Metric:**

- Ít nhất 90% ticket được gợi ý đúng nhóm xử lý.
- Thời gian triage trung bình dưới 30 giây/ticket.
- Các trường hợp pháp lý, tranh chấp hoặc an toàn phải chuyển người phụ trách duyệt.

**Quick Architecture:** LLM Feature + Rule Router.

---

## Quick Problem Card #3 — VinFast: Phân loại mô tả lỗi xe

**Bài toán:** Khách hàng mô tả lỗi xe bằng tiếng Việt tự nhiên, khiến nhân viên hỗ trợ mất thời gian chuyển đổi mô tả thành nhóm lỗi kỹ thuật ban đầu.

**Công ty thành viên:** VinFast

**Actor:** Nhân viên CSKH/kỹ thuật viên tiếp nhận.

### Workflow thủ công hiện tại

1. Khách hàng mô tả triệu chứng.
2. Nhân viên hỏi thêm thông tin.
3. Nhân viên tra tài liệu/mã nhóm lỗi.
4. Chọn bộ phận hoặc kỹ thuật viên phù hợp.
5. Tạo ticket kiểm tra.

**Bottleneck:** Bước 2–4, ước tính 5–8 phút/ticket.

**AI có thể hỗ trợ:** Tóm tắt triệu chứng, gợi ý nhóm lỗi và câu hỏi follow-up chuẩn hóa.

**Success Metric:**

- Giảm thời gian triage xuống dưới 2 phút/ticket.
- Ít nhất 90% ticket được route đúng nhóm kỹ thuật ở vòng đầu.
- AI không được tự kết luận lỗi an toàn nghiêm trọng hoặc đưa lệnh sửa chữa cuối cùng.

**Quick Architecture:** LLM Feature + HITL.

---

# Lựa chọn cho Deep Dive

Chọn **Quick Problem Card #1 — Xanh SM: Điều phối sự cố pin thấp**.

## Lý do

1. Bài toán có workflow cụ thể, dễ xác định bottleneck và metric.
2. Có thể kết hợp rule-based cho điều kiện an toàn với LLM để tạo draft.
3. Ranh giới vận hành rõ: pin < 5%, khoảng cách > 5 km, bắt buộc Human-in-the-loop.
4. Có thể stress-test trực tiếp bằng prompt adversarial trong `starter-code/prompt_prototype.py`.