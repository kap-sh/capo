"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#InvalidStateException``."""

import zapros
from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, ServiceError


class InvalidStateException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidStateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidStateException_.message required")
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.verifiedpermissions#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(
        self,
        data: InvalidStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidStateException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
