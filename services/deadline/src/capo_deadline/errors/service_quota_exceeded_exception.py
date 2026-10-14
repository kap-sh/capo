"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_deadline.types.exception_context
    import capo_deadline.types.service_quota_exceeded_exception_reason
    import capo_deadline.types.string


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "capo_deadline.types.string.String"
    reason: "capo_deadline.types.service_quota_exceeded_exception_reason.ServiceQuotaExceededExceptionReason"
    """<p>A string that describes the reason the quota was exceeded.</p>"""
    resource_type: "capo_deadline.types.string.String"
    """<p>The type of the affected resource</p>"""
    service_code: "capo_deadline.types.string.String"
    """<p>Identifies the service that exceeded the quota.</p>"""
    quota_code: "capo_deadline.types.string.String"
    """<p>Identifies the quota that has been exceeded.</p>"""
    resource_id: NotRequired["capo_deadline.types.string.String"]
    """<p>The identifier of the affected resource.</p>"""
    context: NotRequired["capo_deadline.types.exception_context.ExceptionContext"]
    """<p>Information about the resources in use when the exception was thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_deadline.types.service_quota_exceeded_exception_reason

    out["reason"] = (
        capo_deadline.types.service_quota_exceeded_exception_reason.serialize_json(
            value["reason"]
        )
    )
    out["resourceType"] = value["resource_type"]
    out["serviceCode"] = value["service_code"]
    out["quotaCode"] = value["quota_code"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "context" in value:
        import capo_deadline.types.exception_context

        out["context"] = capo_deadline.types.exception_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if data.get("reason") is not None:
        import capo_deadline.types.service_quota_exceeded_exception_reason

        out["reason"] = (
            capo_deadline.types.service_quota_exceeded_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ServiceQuotaExceededException_.reason required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.resource_type required"
        )
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("context") is not None:
        import capo_deadline.types.exception_context

        out["context"] = capo_deadline.types.exception_context.deserialize_json(
            data["context"]
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.deadline#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(
        self,
        data: ServiceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
