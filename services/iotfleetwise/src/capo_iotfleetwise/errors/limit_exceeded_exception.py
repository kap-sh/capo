"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#LimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.string


class LimitExceededException_(TypedDict, closed=True):
    message: "capo_iotfleetwise.types.string.string"
    resource_id: "capo_iotfleetwise.types.string.string"
    """<p>The identifier of the resource that was exceeded.</p>"""
    resource_type: "capo_iotfleetwise.types.string.string"
    """<p>The type of resource that was exceeded.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("LimitExceededException_.message required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("LimitExceededException_.resource_id required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("LimitExceededException_.resource_type required")
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(
        self,
        data: LimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LimitExceededException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
