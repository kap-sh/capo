"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#IllegalStateException``."""

import zapros
from typing_extensions import TypedDict

from capo_arc_region_switch.errors import DeserializationError, ServiceError


class IllegalStateException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IllegalStateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IllegalStateException_:
    out: IllegalStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("IllegalStateException_.message required")
    return out


class IllegalStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arcregionswitch#IllegalStateException``."""

    code: str | None = "IllegalStateException"

    def __init__(
        self,
        data: IllegalStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IllegalStateException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
