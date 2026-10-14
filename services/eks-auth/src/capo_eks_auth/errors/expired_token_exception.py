"""Generated from Smithy shape ``com.amazonaws.eksauth#ExpiredTokenException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eks_auth.errors import ServiceError


class ExpiredTokenException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ExpiredTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ExpiredTokenException_:
    out: ExpiredTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ExpiredTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eksauth#ExpiredTokenException``."""

    code: str | None = "ExpiredTokenException"

    def __init__(
        self,
        data: ExpiredTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ExpiredTokenException":
        return cls(deserialize_json(data), message, response=response)
