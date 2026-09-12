# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

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
---

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

---

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

---

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`.*
