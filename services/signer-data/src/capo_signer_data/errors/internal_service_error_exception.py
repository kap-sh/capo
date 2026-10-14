"""Generated from Smithy shape ``com.amazonaws.signerdata#InternalServiceErrorException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_signer_data.errors import ServiceError


class InternalServiceErrorException_(TypedDict, closed=True):
    message: NotRequired["str"]
    code: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalServiceErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> InternalServiceErrorException_:
    out: InternalServiceErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    return out


class InternalServiceErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.signerdata#InternalServiceErrorException``."""

    code: str | None = "InternalServiceErrorException"

    def __init__(
        self,
        data: InternalServiceErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServiceErrorException":
        return cls(deserialize_json(data), message, response=response)
