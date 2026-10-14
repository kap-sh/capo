"""Generated from Smithy shape ``com.amazonaws.devopsguru#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_devops_guru.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_devops_guru.types.error_message_string
    import capo_devops_guru.types.error_quota_code_string
    import capo_devops_guru.types.error_service_code_string
    import capo_devops_guru.types.retry_after_seconds


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_devops_guru.types.error_message_string.ErrorMessageString"
    quota_code: NotRequired[
        "capo_devops_guru.types.error_quota_code_string.ErrorQuotaCodeString"
    ]
    """<p> The code of the quota that was exceeded, causing the throttling exception. </p>"""
    service_code: NotRequired[
        "capo_devops_guru.types.error_service_code_string.ErrorServiceCodeString"
    ]
    """<p> The code of the service that caused the throttling exception. </p>"""
    retry_after_seconds: "capo_devops_guru.types.retry_after_seconds.RetryAfterSeconds"
    """<p> The number of seconds after which the action that caused the throttling exception can be retried. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsguru#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)
