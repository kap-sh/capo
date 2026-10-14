"""Generated from Smithy shape ``com.amazonaws.internetmonitor#InternalServerErrorException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import ServiceError


class InternalServerErrorException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.internetmonitor#InternalServerErrorException``."""

    code: str | None = "InternalServerErrorException"

    def __init__(
        self,
        data: InternalServerErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=True,
            code="InternalServerErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerErrorException":
        return cls(deserialize_json(data), message, response=response)
