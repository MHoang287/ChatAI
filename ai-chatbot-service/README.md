1. Tạo venv Python 3.13.9
   python -m venv .venv
   .venv\Scripts\activate (Windows)

2. Cài thư viện:
   pip install -r requirements.txt

3. Chạy server:
   uvicorn main:app --host 0.0.0.0 --port 9000 --reload

4. Test nhanh (Postman / curl):
   POST http://localhost:9000/api/ask
   body JSON:
   { "question": "em quên mật khẩu" }
