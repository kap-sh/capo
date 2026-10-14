"""Generated from Smithy shape ``com.amazonaws.mgn#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import ServiceError

if TYPE_CHECKING:
    import capo_mgn.types.conflict_exception_errors
    import capo_mgn.types.large_bounded_string


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    code: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    resource_id: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>A conflict occurred when prompting for the Resource ID.</p>"""
    resource_type: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>A conflict occurred when prompting for resource type.</p>"""
    errors: NotRequired[
        "capo_mgn.types.conflict_exception_errors.ConflictExceptionErrors"
    ]
    """<p>Conflict Exception specific errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "errors" in value:
        import capo_mgn.types.conflict_exception_errors

        out["errors"] = capo_mgn.types.conflict_exception_errors.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("errors") is not None:
        import capo_mgn.types.conflict_exception_errors

        out["errors"] = capo_mgn.types.conflict_exception_errors.deserialize_json(
            data["errors"]
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#ConflictException``."""

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
