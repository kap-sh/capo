"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import ServiceError

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.exception_message
    import capo_ssm_incidents.types.resource_type


class ConflictException_(TypedDict, closed=True):
    message: "capo_ssm_incidents.types.exception_message.ExceptionMessage"
    resource_identifier: NotRequired["str"]
    """The identifier of the requested resource"""
    resource_type: NotRequired["capo_ssm_incidents.types.resource_type.ResourceType"]
    """The resource type"""
    retry_after: NotRequired["datetime.datetime"]
    """If present in the output, the operation can be retried after this time"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "resource_identifier" in value:
        out["resourceIdentifier"] = value["resource_identifier"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "retry_after" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        out["retryAfter"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["retry_after"]
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("retryAfter") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["retry_after"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["retryAfter"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmincidents#ConflictException``."""

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
