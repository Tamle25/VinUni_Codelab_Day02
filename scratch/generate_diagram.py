import sys
from PIL import Image, ImageDraw, ImageFont

def create_workflow_diagram(output_path="04-workflow-diagram.png"):
    width, height = 1200, 650
    # Background - dark sleek modern background
    img = Image.new("RGB", (width, height), color="#0F172A")
    draw = ImageDraw.Draw(img)

    # Try loading default font
    try:
        font_title = ImageFont.truetype("arial.ttf", 26)
        font_subtitle = ImageFont.truetype("arial.ttf", 16)
        font_header = ImageFont.truetype("arial.ttf", 18)
        font_body = ImageFont.truetype("arial.ttf", 14)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except Exception:
        font_title = font_subtitle = font_header = font_body = font_small = ImageFont.load_default()

    # Draw Title Bar
    draw.rectangle([0, 0, width, 80], fill="#1E293B")
    draw.text((40, 20), "Vin Smart Future — Xanh SM Intelligent Dispatcher", fill="#38BDF8", font=font_title)
    draw.text((40, 52), "Current-State Workflow Mapping (Sơ đồ quy trình thủ công hiện tại)", fill="#94A3B8", font=font_subtitle)

    # Steps Configuration
    steps = [
        {"num": "1", "title": "Nhận cuộc gọi sự cố", "actor": "Dispatcher", "time": "⏱ 2 min", "in": "In: Điện thoại", "out": "Out: Log sự cố", "color": "#3B82F6", "is_bottleneck": False},
        {"num": "2", "title": "Tra cứu định vị GPS", "actor": "Dispatcher", "time": "⏱ 2 min", "in": "In: Biển số xe", "out": "Out: Tọa độ GPS", "color": "#3B82F6", "is_bottleneck": False},
        {"num": "3", "title": "Tra cứu trạm sạc trống", "actor": "Dispatcher", "time": "⏱ 5 min", "in": "In: GPS + Dòng xe", "out": "Out: Địa chỉ trạm", "color": "#EF4444", "is_bottleneck": True},
        {"num": "4", "title": "Soạn tin nhắn hướng dẫn", "actor": "Dispatcher", "time": "⏱ 5 min", "in": "In: Data trạm sạc", "out": "Out: SMS / App msg", "color": "#EF4444", "is_bottleneck": True},
        {"num": "5", "title": "Gọi xe cứu hộ (nếu cần)", "actor": "Dispatcher", "time": "⏱ 1 min", "in": "In: Pin < 5%", "out": "Out: Dispatch cứu hộ", "color": "#10B981", "is_bottleneck": False},
    ]

    card_w = 200
    card_h = 240
    start_x = 40
    gap_x = 35
    start_y = 160

    for i, step in enumerate(steps):
        x = start_x + i * (card_w + gap_x)
        y = start_y

        # Border & Card Fill
        border_col = step["color"]
        fill_col = "#1E293B" if not step["is_bottleneck"] else "#2D1B24"
        
        draw.rectangle([x, y, x + card_w, y + card_h], fill=fill_col, outline=border_col, width=3)
        
        # Step Header Pill
        pill_text = f"Bước {step['num']}" + (" 🔴 BOTTLENECK" if step["is_bottleneck"] else "")
        draw.rectangle([x + 10, y + 12, x + card_w - 10, y + 42], fill=border_col)
        draw.text((x + 20, y + 18), pill_text, fill="#FFFFFF", font=font_small)

        # Content
        draw.text((x + 15, y + 55), step["title"], fill="#F8FAFC", font=font_header)
        draw.text((x + 15, y + 95), f"Người thực hiện: {step['actor']}", fill="#CBD5E1", font=font_body)
        draw.text((x + 15, y + 125), f"Thời gian: {step['time']}", fill="#F59E0B" if step["is_bottleneck"] else "#10B981", font=font_header)
        
        draw.line([x + 15, y + 155, x + card_w - 15, y + 155], fill="#475569", width=1)
        
        draw.text((x + 15, y + 165), step["in"], fill="#94A3B8", font=font_small)
        draw.text((x + 15, y + 195), step["out"], fill="#94A3B8", font=font_small)

        # Draw Connecting Arrow
        if i < len(steps) - 1:
            arrow_start_x = x + card_w
            arrow_end_x = arrow_start_x + gap_x
            arrow_y = y + card_h // 2
            
            draw.line([arrow_start_x + 5, arrow_y, arrow_end_x - 5, arrow_y], fill="#64748B", width=3)
            # Arrow head
            draw.polygon([
                (arrow_end_x - 5, arrow_y - 6),
                (arrow_end_x + 2, arrow_y),
                (arrow_end_x - 5, arrow_y + 6)
            ], fill="#64748B")
            
            # Handoff label
            draw.text((arrow_start_x + 8, arrow_y - 20), "🔄", fill="#F59E0B", font=font_small)

    # Footer Stats Summary
    summary_y = 440
    draw.rectangle([40, summary_y, width - 40, summary_y + 160], fill="#1E293B", outline="#334155", width=2)
    
    draw.text((60, summary_y + 20), "📊 TỔNG QUAN BOTTLENECK & HIỆU SUẤT VẬN HÀNH THỦ CÔNG", fill="#F8FAFC", font=font_header)
    
    stats = [
        "🔴 Bottleneck nghiêm trọng: Bước 3 (Tra cứu trụ sạc trống) & Bước 4 (Soạn tin nhắn hướng dẫn). Tốn 10 phút/lượt.",
        "⏱ Tổng thời gian xử lý thủ công: 15 phút / sự cố thực địa (Gây ùn tắc đội xe Xanh SM giờ cao điểm).",
        "💡 Mục tiêu AI Fit (LLM Feature): Tự động hóa Bước 3 & 4 ──> Giảm thời gian xử lý xuống dưới 3 phút/lượt."
    ]
    
    for idx, stat_text in enumerate(stats):
        draw.text((60, summary_y + 55 + idx * 32), stat_text, fill="#CBD5E1", font=font_body)

    img.save(output_path)
    print(f"Workflow diagram saved successfully at {output_path}")

if __name__ == "__main__":
    create_workflow_diagram()
