from typing import Any, Dict, List, Self

from pydantic import BaseModel


class Tapping(BaseModel):
    action_energy: int
    maximum: int
    available: int


class Holding(BaseModel):
    action_energy: List[int]
    maximum: int
    available: int


class Frens(BaseModel):
    count: int
    reward: int
    invite_link: str


class Tasks(BaseModel):
    available: dict
    completed: dict


class User(BaseModel):
    id: int
    balance: int
    tapping: Tapping
    holding: Holding
    frens: Frens
    tasks: Tasks
    boosts: Dict[str, Any]


class Reward(BaseModel):
    balance: int


class UserInfo(BaseModel):
    user: User

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        return cls(**data)


class TapClaimInfo(BaseModel):
    user: User
    reward: Reward

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        return cls(**data)


class CreateInfo(BaseModel):
    user: User
    invite_link: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        return cls(**data)


class HoldStartInfo(BaseModel):
    user: User
    holding_token: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        return cls(**data)


class HoldCheckInfo(BaseModel):
    holding_success: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        return cls(**data)


class HoldClaimInfo(BaseModel):
    user: User
    holding_success: bool
    reward: Reward

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Self:
        return cls(**data)
