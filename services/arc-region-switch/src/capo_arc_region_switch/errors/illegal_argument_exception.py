"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#IllegalArgumentException``."""

import zapros
from typing_extensions import TypedDict

from capo_arc_region_switch.errors import ServiceError


class IllegalArgumentException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IllegalArgumentException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IllegalArgumentException_:
    out: IllegalArgumentException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class IllegalArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arcregionswitch#IllegalArgumentException``."""

    code: str | None = "IllegalArgumentException"

    def __init__(
        self,
        data: IllegalArgumentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalArgumentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IllegalArgumentException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
