"""Generated from Smithy shape ``com.amazonaws.panorama#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_panorama.types.conflict_exception_error_argument_list
    import capo_panorama.types.string


class ConflictException_(TypedDict, closed=True):
    message: "capo_panorama.types.string.String"
    resource_id: "capo_panorama.types.string.String"
    """<p>The resource's ID.</p>"""
    resource_type: "capo_panorama.types.string.String"
    """<p>The resource's type.</p>"""
    error_id: NotRequired["capo_panorama.types.string.String"]
    """<p>A unique ID for the error.</p>"""
    error_arguments: NotRequired[
        "capo_panorama.types.conflict_exception_error_argument_list.ConflictExceptionErrorArgumentList"
    ]
    """<p>A list of attributes that led to the exception and their values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "error_id" in value:
        out["ErrorId"] = value["error_id"]
    if "error_arguments" in value:
        import capo_panorama.types.conflict_exception_error_argument_list

        out["ErrorArguments"] = (
            capo_panorama.types.conflict_exception_error_argument_list.serialize_json(
                value["error_arguments"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    if data.get("ErrorId") is not None:
        out["error_id"] = data["ErrorId"]
    if data.get("ErrorArguments") is not None:
        import capo_panorama.types.conflict_exception_error_argument_list

        out["error_arguments"] = (
            capo_panorama.types.conflict_exception_error_argument_list.deserialize_json(
                data["ErrorArguments"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.panorama#ConflictException``."""

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
