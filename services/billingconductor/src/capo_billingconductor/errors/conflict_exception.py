"""Generated from Smithy shape ``com.amazonaws.billingconductor#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import ServiceError

if TYPE_CHECKING:
    import capo_billingconductor.types.conflict_exception_reason
    import capo_billingconductor.types.string


class ConflictException_(TypedDict, closed=True):
    message: "capo_billingconductor.types.string.String"
    resource_id: "capo_billingconductor.types.string.String"
    """<p>Identifier of the resource in use. </p>"""
    resource_type: "capo_billingconductor.types.string.String"
    """<p>Type of the resource in use. </p>"""
    reason: NotRequired[
        "capo_billingconductor.types.conflict_exception_reason.ConflictExceptionReason"
    ]
    """<p>Reason for the inconsistent state. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["ResourceId"] = value["resource_id"]
    out["ResourceType"] = value["resource_type"]
    if "reason" in value:
        import capo_billingconductor.types.conflict_exception_reason

        out["Reason"] = (
            capo_billingconductor.types.conflict_exception_reason.serialize_json(
                value["reason"]
            )
        )
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
    if data.get("Reason") is not None:
        import capo_billingconductor.types.conflict_exception_reason

        out["reason"] = (
            capo_billingconductor.types.conflict_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billingconductor#ConflictException``."""

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
