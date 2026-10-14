"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#OcuLimitExceededException``."""

import zapros
from typing_extensions import TypedDict

from capo_opensearchserverless.errors import DeserializationError, ServiceError


class OcuLimitExceededException_(TypedDict, closed=True):
    message: "str"
    """Description of the error."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OcuLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> OcuLimitExceededException_:
    out: OcuLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("OcuLimitExceededException_.message required")
    return out


class OcuLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.opensearchserverless#OcuLimitExceededException``."""

    code: str | None = "OcuLimitExceededException"

    def __init__(
        self,
        data: OcuLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OcuLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "OcuLimitExceededException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
