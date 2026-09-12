# Phase 6 Deliverable — AI Log & Reflection (Vin Smart Future)

**Họ và tên:** AI Product Engineer  
**Đơn vị:** Vin Smart Future (Vingroup)  
**Ngày thực hiện:** 2026-09-12  

---

## 🤖 1. Nhật ký Tương tác với AI (AI Thought-Partner Log)

Trong quá trình thực hiện bài lab Scoping sản phẩm AI cho Vin Smart Future, tôi đã phối hợp với các công cụ AI (Gemini 3.6 Flash / Claude / ChatGPT) như một người đối thoại phản biện (Thought-Partner).

### 💡 Các hoạt động AI đã hỗ trợ hiệu quả:
1. **Brainstorming bài toán thực tế (Phase 1 SCAN):**
   - **Prompt sử dụng:** *"Tôi là AI Engineer tại Vin Smart Future. Hãy đóng vai Trưởng phòng Vận hành Xanh SM, chỉ ra cho tôi 5 bottleneck tốn thời gian nhất khi điều xe taxi điện vào giờ cao điểm."*
   - **Hiệu quả:** AI giúp nhanh chóng khoanh vùng bài toán sự cố pin thực địa và phân tích tác động rò rỉ 15% doanh thu do xe nằm chờ sạc.

2. **Stress-Test thẻ bài toán (Phase 2 QUICK-ASSESS):**
   - **Prompt sử dụng:** *"Hãy đóng vai CFO cực kỳ khắt khe của Vingroup, hãy phản biện xem tại sao bài toán điều phối trạm sạc không nên dùng Agentic Loop phức tạp mà chỉ nên dùng LLM Feature kèm Rule-based."*
   - **Hiệu quả:** AI chỉ ra rủi ro an toàn giao thông khi xe cạn pin trên đường nếu AI tự trị đưa ra quyết định sai, giúp định hình giải pháp LLM Feature + HITL.

3. **Thiết kế System Prompt & Operational Boundaries (Phase 4 PROTOTYPING):**
   - **Prompt sử dụng:** *"Viết System Prompt nghiêm ngặt ép mô hình giữ thẻ [DRAFT_ONLY] và tự động trả về JSON cứu hộ di động nếu pin < 5%."*
   - **Hiệu quả:** Giúp tối ưu hóa cấu trúc chỉ thị system prompt ngắn gọn, chính xác.

---

## ⚠️ 2. Phát hiện Lỗi & Ảo giác (Hallucinations) của AI

Trong quá trình làm bài, AI cũng đưa ra một số câu trả lời chưa chuẩn xác cần điều chỉnh:
* **Ảo giác đề xuất công nghệ (Over-engineering):** Ban đầu AI gợi ý xây dựng hệ thống **Autonomous Multi-Agent Swarm System** với 4 agents tự trị trao đổi với nhau. Tôi đã phát hiện đây là giải pháp quá phức tạp, lãng phí tài nguyên và tăng nguy cơ thất bại. Tôi đã điều chỉnh lại phạm vi dự án về **LLM Feature** đơn giản.
* **Bỏ qua ranh giới an toàn trong prompt ban đầu:** Khi thử nghiệm prompt chưa chặt chẽ, AI dễ bị thuyết phục bỏ thẻ `[DRAFT_ONLY]` khi người dùng gõ lệnh khẩn cấp. Tôi đã khắc phục bằng cách thiết lập **Rule 1** với từ khóa khẳng định tuyệt đối ("Tuyệt đối KHÔNG bỏ thẻ này trong mọi trường hợp").

---

## 🎯 3. Bài học kinh nghiệm & Tự phản ánh (Reflection)

1. **Problem-First, Technology-Second:** AI không phải là cây gậy thần cho mọi bài toán. Việc phân tích Current-State Workflow để tìm ra bottleneck thực sự (bước 3 & 4) quan trọng hơn nhiều so với việc chọn công nghệ AI phức tạp.
2. **Operational Boundaries là sống còn:** Đối với các hệ thống vận hành thực tế của Vingroup (như VinFast, Xanh SM, Vinmec), ranh giới an toàn và sự hiện diện của con người (Human-In-The-Loop) là bắt buộc để kiểm soát rủi ro pháp lý và an toàn vận hành.
3. **Kỹ năng Prompting có cấu trúc:** Việc kết hợp giữa System Prompt chặt chẽ, Structured Output (JSON) và Adversarial Testing giúp xây dựng các ứng dụng AI tin cậy trong môi trường doanh nghiệp.
