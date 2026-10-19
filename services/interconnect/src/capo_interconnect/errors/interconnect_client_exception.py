"""Generated from Smithy shape ``com.amazonaws.interconnect#InterconnectClientException``."""

import zapros
from typing_extensions import TypedDict

from capo_interconnect.errors import ServiceError


class InterconnectClientException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InterconnectClientException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InterconnectClientException_:
    out: InterconnectClientException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class InterconnectClientException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.interconnect#InterconnectClientException``."""

    code: str | None = "InterconnectClientException"

    def __init__(
        self,
        data: InterconnectClientException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InterconnectClientException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InterconnectClientException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
