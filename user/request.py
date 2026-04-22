from pydantic import BaseModel

# 회원가입 요청에 필요한 데이터 형식
class SignUpRequest(BaseModel):
    email: str
    password: str

# 로그인에 필요한 데이터 형식
class LoginRequest(BaseModel):
    email: str
    password: str

# 아래처럼 공유해서 쓸 수 있지만, 나누는 것을 추천
# 각각의 api가 어떤 식으로 바뀔지도 모르고 이런저런 이유 등등 때문.
# class AuthRequest(BaseModel):
#     email: str
#     password: str

# 건강 프로필 생성에 필요한 데이터 형식
class HealthProfileRequest(BaseModel):
    age: int
    height_cm: float
    weight_kg: float
    smoking: bool
    exercise_per_week: int