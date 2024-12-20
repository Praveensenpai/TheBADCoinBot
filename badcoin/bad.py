from badcoin.endpoints import Endpoints
from badcoin.headers import COMMON_HEADERS
from badcoin.models import (
    HoldCheckInfo,
    HoldClaimInfo,
    HoldStartInfo,
    TapClaimInfo,
    CreateInfo,
    UserInfo,
)
from env import Env
import requests


class BAD:
    def __init__(self, web_app_data: str):
        self.web_app_data = web_app_data
        self.session = requests.Session()

    def tap(self) -> TapClaimInfo:
        resp = self.session.post(
            Endpoints.TAP_CLAIM_URL,
            headers={
                **COMMON_HEADERS,
                "Authorization": f"tma {self.web_app_data}",
            },
        )
        return TapClaimInfo.from_dict(resp.json())

    def info(self) -> UserInfo:
        resp = self.session.post(
            Endpoints.INFO_URL,
            headers={
                **COMMON_HEADERS,
                "Authorization": f"tma {self.web_app_data}",
            },
        )
        return UserInfo.from_dict(resp.json())

    def create(self) -> CreateInfo:
        resp = self.session.post(
            Endpoints.CREATE_URL,
            headers={
                **COMMON_HEADERS,
                "Authorization": f"tma {self.web_app_data}",
            },
            json={"invite_code": Env.REF_ID},
        )
        return CreateInfo.from_dict(resp.json())

    def hold_start(self) -> HoldStartInfo:
        resp = self.session.post(
            Endpoints.HOLD_START_URL,
            headers={
                **COMMON_HEADERS,
                "Authorization": f"tma {self.web_app_data}",
            },
        )
        return HoldStartInfo.from_dict(resp.json())

    def hold_check(self, holding_checkpoint: int, holding_token: str) -> HoldCheckInfo:
        resp = self.session.post(
            Endpoints.HOLD_CHECK_URL,
            headers={
                **COMMON_HEADERS,
                "Authorization": f"tma {self.web_app_data}",
            },
            json={
                "holding_checkpoint": holding_checkpoint,
                "holding_token": holding_token,
            },
        )
        return HoldCheckInfo.from_dict(resp.json())

    def hold_claim(self, holding_checkpoint: int, holding_token: str) -> HoldClaimInfo:
        resp = self.session.post(
            Endpoints.HOLD_CLAIM_URL,
            headers={
                **COMMON_HEADERS,
                "Authorization": f"tma {self.web_app_data}",
            },
            json={
                "holding_checkpoint": holding_checkpoint,
                "holding_token": holding_token,
            },
        )
        return HoldClaimInfo.from_dict(resp.json())
