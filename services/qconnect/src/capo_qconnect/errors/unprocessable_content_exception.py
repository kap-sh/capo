"""Generated from Smithy shape ``com.amazonaws.qconnect#UnprocessableContentException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import ServiceError


class UnprocessableContentException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableContentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnprocessableContentException_:
    out: UnprocessableContentException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class UnprocessableContentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qconnect#UnprocessableContentException``."""

    code: str | None = "UnprocessableContentException"

    def __init__(
        self,
        data: UnprocessableContentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnprocessableContentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnprocessableContentException":
        return cls(deserialize_json(data), message, response=response)
