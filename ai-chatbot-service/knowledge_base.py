# knowledge_base.py
# =======================
# Danh sách Q&A liên quan đến hệ thống học trực tuyến ASP.NET MVC
# Bạn có thể thêm/sửa các câu hỏi và keywords dễ dàng.

FAQ_DATA = [
    # 🧩 Tài khoản & Đăng nhập
    {
        "question": "Tôi quên mật khẩu, làm sao lấy lại?",
        "keywords": ["quen mat khau", "quên mật khẩu", "reset pass", "đặt lại mật khẩu"],
        "answer": (
            "Vào trang Đăng nhập → chọn 'Quên mật khẩu'. Nhập email đã đăng ký, "
            "hệ thống sẽ gửi link đặt lại mật khẩu qua email (kiểm tra cả thư rác)."
        ),
    },
    {
        "question": "Tôi chưa nhận email xác nhận tài khoản?",
        "keywords": ["chưa nhận email", "xác nhận tài khoản", "verify email", "confirm email"],
        "answer": (
            "Sau khi đăng ký, nếu chưa nhận được email xác nhận, "
            "bạn có thể vào lại trang Đăng nhập, nhấn 'Gửi lại email xác nhận'."
        ),
    },
    {
        "question": "Tài khoản mới có quyền gì?",
        "keywords": ["role", "quyền", "vai trò", "teacher hay user", "admin hay user"],
        "answer": (
            "Mặc định tài khoản mới sẽ là User (Học viên). "
            "Chỉ có Admin mới có quyền nâng cấp lên Teacher hoặc Admin."
        ),
    },
    {
        "question": "Làm sao chỉnh sửa hồ sơ cá nhân?",
        "keywords": ["sửa hồ sơ", "đổi tên", "avatar", "ảnh đại diện", "hồ sơ cá nhân"],
        "answer": (
            "Vào menu tài khoản → chọn 'Hồ sơ cá nhân'. "
            "Tại đây bạn có thể đổi họ tên, ảnh đại diện, ngày sinh và địa chỉ."
        ),
    },

    # 🎓 Khóa học
    {
        "question": "Làm sao xem danh sách khóa học?",
        "keywords": ["xem khóa học", "danh sách khóa học", "list khóa học", "tìm khóa học"],
        "answer": (
            "Vào trang 'Tất cả khóa học' ở thanh điều hướng. "
            "Bạn có thể lọc theo danh mục, giá, mức độ, giảng viên hoặc tìm bằng từ khóa."
        ),
    },
    {
        "question": "Có xem thử video trước khi mua không?",
        "keywords": ["xem thử", "preview", "video giới thiệu", "coi thử"],
        "answer": "Có, mỗi khóa học đều có video giới thiệu miễn phí để bạn xem trước khi đăng ký.",
    },
    {
        "question": "Làm sao xem khóa học tôi đã mua?",
        "keywords": ["khóa học của tôi", "my courses", "đã mua"],
        "answer": (
            "Vào menu tài khoản → chọn 'Khóa học của tôi' để xem danh sách khóa học bạn đã đăng ký hoặc mua."
        ),
    },
    {
        "question": "Làm sao xem khóa học phổ biến?",
        "keywords": ["khóa học phổ biến", "nhiều người học", "trending"],
        "answer": "Truy cập mục 'Phổ biến' trên thanh menu để xem các khóa học có lượt học cao nhất.",
    },

    # 💸 Thanh toán & Hoàn tiền
    {
        "question": "Thanh toán bằng MoMo như thế nào?",
        "keywords": ["thanh toán", "momo", "trả tiền", "payment", "mua khóa học"],
        "answer": (
            "Khi mua khóa học, chọn phương thức thanh toán 'MoMo' và quét mã hoặc truy cập link: "
            "https://me.momo.vn/xoanws để hoàn tất. Hệ thống sẽ tự kích hoạt khóa học sau khi thanh toán thành công."
        ),
    },
    {
        "question": "Nếu thanh toán thất bại thì sao?",
        "keywords": ["thanh toán lỗi", "thanh toán thất bại", "momo lỗi", "payment failed"],
        "answer": (
            "Hãy kiểm tra lại kết nối mạng hoặc ví MoMo. Nếu vẫn không được, "
            "liên hệ qua email support@onlinelearning.vn để được hỗ trợ."
        ),
    },
    {
        "question": "Có được hoàn tiền không?",
        "keywords": ["hoàn tiền", "refund", "trả lại tiền"],
        "answer": (
            "Bạn có thể yêu cầu hoàn tiền trong 24h kể từ khi kích hoạt khóa học và chưa học quá 20% nội dung. "
            "Admin sẽ xem xét và xử lý thủ công."
        ),
    },

    # 📡 Livestream
    {
        "question": "Livestream hoạt động như thế nào?",
        "keywords": ["livestream", "xem live", "phòng live", "giảng viên live"],
        "answer": (
            "Mỗi giảng viên có một phòng livestream riêng. Khi giảng viên đang phát, "
            "bạn có thể vào mục 'Vào Livestream' để tham gia xem và chat trực tiếp."
        ),
    },
    {
        "question": "Học viên khác mạng có xem livestream được không?",
        "keywords": ["khác mạng", "ngoài mạng", "không cùng wifi", "xem live không được"],
        "answer": (
            "Có. Livestream được truyền qua hệ thống WebRTC, bạn chỉ cần vào link ngrok public "
            "do website cung cấp để xem bình thường."
        ),
    },
    {
        "question": "Giảng viên bắt đầu livestream như thế nào?",
        "keywords": ["bắt đầu livestream", "start live", "giảng viên phát live"],
        "answer": (
            "Giảng viên vào menu Giảng viên → Livestream → 'Bắt đầu Livestream'. "
            "Hệ thống sẽ tự tạo phòng và cấp link xem cho học viên."
        ),
    },

    # 🧾 Bài tập & Kiểm tra
    {
        "question": "Làm sao nộp bài tập?",
        "keywords": ["bài tập", "nộp bài", "upload bài", "assignment"],
        "answer": (
            "Trong trang khóa học, chọn mục 'Bài tập' → chọn bài cần làm → nhấn 'Nộp bài'. "
            "Bạn có thể tải lại file nếu chưa hết hạn nộp."
        ),
    },
    {
        "question": "Làm sao làm bài kiểm tra?",
        "keywords": ["kiểm tra", "quiz", "test", "thi"],
        "answer": (
            "Trong trang khóa học, chọn mục 'Kiểm tra' → hệ thống sẽ hiển thị câu hỏi trắc nghiệm. "
            "Sau khi hoàn thành, bạn có thể xem điểm ngay."
        ),
    },
    {
        "question": "Tôi có thể xem điểm và thống kê không?",
        "keywords": ["xem điểm", "thống kê", "kết quả học tập"],
        "answer": (
            "Bạn vào trang cá nhân → 'Tiến độ học tập' để xem điểm, "
            "số bài đã hoàn thành và biểu đồ thống kê chi tiết."
        ),
    },

    # 🧾 Chứng chỉ & Hoàn thành
    {
        "question": "Làm sao nhận chứng chỉ hoàn thành?",
        "keywords": ["chứng chỉ", "certificate", "hoàn thành"],
        "answer": (
            "Khi bạn hoàn thành 100% bài học và bài kiểm tra, hệ thống sẽ tự tạo chứng chỉ "
            "dưới dạng PDF. Bạn có thể tải tại trang 'Tiến độ học tập'."
        ),
    },

    # 🔔 Thông báo & Hệ thống
    {
        "question": "Làm sao xem thông báo?",
        "keywords": ["thông báo", "notification", "tin nhắn hệ thống"],
        "answer": (
            "Nhấn biểu tượng chuông 🔔 ở thanh điều hướng. Các thông báo chưa đọc sẽ có dấu đỏ. "
            "Bạn cũng có thể đánh dấu tất cả là đã đọc."
        ),
    },

    # ⚙️ Kỹ thuật & AI Chatbot
    {
        "question": "Website chạy được trên điện thoại không?",
        "keywords": ["điện thoại", "mobile", "smartphone", "responsive"],
        "answer": (
            "Có, website hỗ trợ giao diện responsive (Bootstrap 5), tương thích tốt trên điện thoại và máy tính bảng."
        ),
    },
    {
        "question": "Chat AI hoạt động thế nào?",
        "keywords": ["chat ai", "chatbot", "trí tuệ nhân tạo", "hỏi đáp"],
        "answer": (
            "Chat AI sử dụng Python FastAPI để xử lý câu hỏi, và ASP.NET MVC gọi API qua Reverse Proxy. "
            "AI sẽ trả lời các câu hỏi liên quan đến hệ thống học trực tuyến của bạn."
        ),
    },
    {
        "question": "Dữ liệu chat có được lưu lại không?",
        "keywords": ["lưu chat", "bảo mật", "riêng tư", "privacy"],
        "answer": (
            "Các câu hỏi có thể được ghi log nội bộ để cải thiện hệ thống. "
            "Chúng tôi không thu thập thông tin cá nhân nhạy cảm."
        ),
    },
]


def find_best_answer(user_question: str) -> dict:
    """Tìm câu trả lời khớp nhất theo từ khóa"""
    uq = user_question.lower().strip()
    best = None
    best_score = 0

    for item in FAQ_DATA:
        score = 0
        for kw in item["keywords"]:
            if kw.lower() in uq:
                score += 1
        if score > best_score:
            best_score = score
            best = item

    if best and best_score > 0:
        return {
            "answer": best["answer"],
            "matched_question": best["question"],
            "score": best_score
        }

    return {
        "answer": (
            "Xin lỗi, mình chưa có câu trả lời cho câu hỏi này.\n"
            "Bạn có thể hỏi về: tài khoản, khóa học, thanh toán, livestream, bài tập hoặc chứng chỉ."
        ),
        "matched_question": None,
        "score": 0
    }
