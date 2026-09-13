# FastAPI Tutorial — Roadmap nâng cao

Dự án bắt đầu: CRUD Todo cơ bản dùng `dict` làm database giả lập (`src/main.py`).
Checklist dưới đây dùng để theo dõi tiến độ — tick `[x]` sau mỗi phần đã làm xong và push.

---

## 1. Pydantic nâng cao & Validation

Tách model cho Create/Update/Response thay vì dùng chung 1 model `Todo` cho mọi việc.

- [x] Tạo `TodoCreate`, `TodoUpdate`, `TodoResponse` riêng biệt
- [x] Dùng `Field()` để validate độ dài, giá trị min/max
- [ ] Thử `field_validator` và `model_validator` (Pydantic v2)
- [ ] Đọc: https://docs.pydantic.dev/latest/concepts/validators/

## 2. Dependency Injection (`Depends`)

Tính năng mạnh nhất của FastAPI — dùng để tách logic DB, auth, pagination ra khỏi route.

- [ ] Viết hàm `get_db()` thay vì dùng biến `db` global
- [ ] Dùng `Depends()` trong path operation
- [ ] Thử class-based dependency
- [ ] Đọc: https://fastapi.tiangolo.com/tutorial/dependencies/

## 3. Database thật với SQLModel/SQLAlchemy

Thay `dict` bằng database thật (SQLite trước, rồi Postgres), dùng async ORM.

- [ ] Cài `sqlmodel` hoặc `sqlalchemy` + `asyncpg`
- [ ] Tạo engine, session, và `Depends(get_session)`
- [ ] Thử Alembic để quản lý migration
- [ ] Đọc: https://sqlmodel.tiangolo.com/tutorial/fastapi/

## 4. Authentication & Security

Thêm đăng nhập, bảo vệ route bằng JWT token — quan trọng cho app thực tế.

- [ ] Học `OAuth2PasswordBearer` + JWT (`python-jose`)
- [ ] Hash password với `passlib`/`bcrypt`
- [ ] Bảo vệ route với `Depends(get_current_user)`
- [ ] Đọc: https://fastapi.tiangolo.com/tutorial/security/

## 5. Xử lý lỗi & Middleware

Viết exception handler tùy chỉnh và middleware để log request/response.

- [ ] Dùng `@app.exception_handler()` cho lỗi custom
- [ ] Viết middleware log thời gian xử lý request
- [ ] Thêm CORS middleware
- [ ] Đọc: https://fastapi.tiangolo.com/tutorial/handling-errors/

## 6. Testing với pytest

Viết test cho API bằng `TestClient`, đảm bảo code không bị lỗi khi refactor.

- [ ] Cài `pytest` + `httpx`
- [ ] Dùng `TestClient(app)` để gọi API giả lập
- [ ] Viết fixture để tạo/xóa dữ liệu test
- [ ] Đọc: https://fastapi.tiangolo.com/tutorial/testing/

## 7. Async & Background Tasks

Tận dụng async thực sự (I/O không block) và xử lý tác vụ nền.

- [ ] Chuyển route sang `async def` khi gọi DB/API ngoài
- [ ] Dùng `BackgroundTasks` cho việc gửi email/log
- [ ] Thử `asyncio.gather()` cho nhiều tác vụ song song
- [ ] Đọc: https://fastapi.tiangolo.com/tutorial/background-tasks/

## 8. Deployment

Đóng gói và triển khai app ra môi trường thật.

- [ ] Viết Dockerfile với `uv` (dự án đã có `uv.lock`)
- [ ] Chạy bằng Uvicorn + Gunicorn workers
- [ ] Thử deploy lên Fly.io/Railway/VPS
- [ ] Đọc: https://fastapi.tiangolo.com/deployment/docker/