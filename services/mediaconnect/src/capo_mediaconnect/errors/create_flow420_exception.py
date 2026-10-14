"""Generated from Smithy shape ``com.amazonaws.mediaconnect#CreateFlow420Exception``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import ServiceError


class CreateFlow420Exception_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlow420Exception_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateFlow420Exception_:
    out: CreateFlow420Exception_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CreateFlow420Exception(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#CreateFlow420Exception``."""

    code: str | None = "CreateFlow420Exception"

    def __init__(
        self,
        data: CreateFlow420Exception_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CreateFlow420Exception",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CreateFlow420Exception":
        return cls(deserialize_json(data), message, response=response)
