"""Generated from Smithy shape ``com.amazonaws.ebs#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ebs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ebs.types.error_message
    import capo_ebs.types.service_quota_exceeded_exception_reason


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_ebs.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "capo_ebs.types.service_quota_exceeded_exception_reason.ServiceQuotaExceededExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_ebs.types.service_quota_exceeded_exception_reason

        out["Reason"] = (
            capo_ebs.types.service_quota_exceeded_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_ebs.types.service_quota_exceeded_exception_reason

        out["reason"] = (
            capo_ebs.types.service_quota_exceeded_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ebs#ServiceQuotaExceededException``."""

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
