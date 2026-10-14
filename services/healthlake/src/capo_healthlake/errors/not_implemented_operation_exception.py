"""Generated from Smithy shape ``com.amazonaws.healthlake#NotImplementedOperationException``."""

import zapros
from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, ServiceError


class NotImplementedOperationException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotImplementedOperationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NotImplementedOperationException_:
    out: NotImplementedOperationException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("NotImplementedOperationException_.message required")
    return out


class NotImplementedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.healthlake#NotImplementedOperationException``."""

    code: str | None = "NotImplementedOperationException"

    def __init__(
        self,
        data: NotImplementedOperationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="NotImplementedOperationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotImplementedOperationException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
