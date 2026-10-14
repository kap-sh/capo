"""Generated from Smithy shape ``com.amazonaws.healthlake#UnsupportedMIMETypeException``."""

import zapros
from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, ServiceError


class UnsupportedMIMETypeException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnsupportedMIMETypeException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnsupportedMIMETypeException_:
    out: UnsupportedMIMETypeException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("UnsupportedMIMETypeException_.message required")
    return out


class UnsupportedMIMETypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.healthlake#UnsupportedMIMETypeException``."""

    code: str | None = "UnsupportedMIMETypeException"

    def __init__(
        self,
        data: UnsupportedMIMETypeException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedMIMETypeException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "UnsupportedMIMETypeException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
