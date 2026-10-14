"""Generated from Smithy shape ``com.amazonaws.interconnect#InterconnectValidationException``."""

import zapros
from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError, ServiceError


class InterconnectValidationException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InterconnectValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InterconnectValidationException_:
    out: InterconnectValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InterconnectValidationException_.message required")
    return out


class InterconnectValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.interconnect#InterconnectValidationException``."""

    code: str | None = "InterconnectValidationException"

    def __init__(
        self,
        data: InterconnectValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InterconnectValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InterconnectValidationException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
