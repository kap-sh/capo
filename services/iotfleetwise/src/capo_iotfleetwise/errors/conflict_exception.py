"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.string


class ConflictException_(TypedDict, closed=True):
    message: "capo_iotfleetwise.types.string.string"
    resource: "capo_iotfleetwise.types.string.string"
    """<p>The resource on which there are conflicting operations.</p>"""
    resource_type: "capo_iotfleetwise.types.string.string"
    """<p>The type of resource on which there are conflicting operations..</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resource"] = value["resource"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("ConflictException_.resource required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
