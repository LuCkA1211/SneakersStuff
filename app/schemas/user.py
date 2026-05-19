from pydantic import BaseModel, Field

class UserResponse(BaseModel):
    username: str
    email: str
    name: str
    surname: str
    address: str
    city: str

    model_config = {"from_attributes": True}

class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=20)
    email: str = Field(..., min_length=4, max_length=30)
    name: str = Field(..., min_length=1, max_length=15)
    surname: str = Field(..., min_length=1, max_length=30)
    password: str  # Hashed
    address: str = Field(..., min_length=5, max_length=30)
    city: str = Field(..., min_length=1, max_length=55)

class UserCreateResponse(BaseModel):
    username: str

class ResponseCreateUser(BaseModel):
    message: str
    user: UserCreateResponse

class TokenUser(BaseModel):
    access_token: str
    token_type: str

class AdminResponse(BaseModel):
    username: str

    model_config = {"from_attributes": True}