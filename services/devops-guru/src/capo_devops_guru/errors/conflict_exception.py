"""Generated from Smithy shape ``com.amazonaws.devopsguru#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_devops_guru.errors import ServiceError

if TYPE_CHECKING:
    import capo_devops_guru.types.error_message_string
    import capo_devops_guru.types.resource_id_string
    import capo_devops_guru.types.resource_id_type


class ConflictException_(TypedDict, closed=True):
    message: "capo_devops_guru.types.error_message_string.ErrorMessageString"
    resource_id: "capo_devops_guru.types.resource_id_string.ResourceIdString"
    """<p> The ID of the Amazon Web Services resource in which a conflict occurred. </p>"""
    resource_type: "capo_devops_guru.types.resource_id_type.ResourceIdType"
    """<p> The type of the Amazon Web Services resource in which a conflict occurred. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsguru#ConflictException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
