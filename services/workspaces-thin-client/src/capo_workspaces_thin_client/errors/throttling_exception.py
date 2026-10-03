"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_thin_client.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces_thin_client.types.exception_message
    import capo_workspaces_thin_client.types.quota_code
    import capo_workspaces_thin_client.types.retry_after_seconds
    import capo_workspaces_thin_client.types.service_code


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_workspaces_thin_client.types.exception_message.ExceptionMessage"
    ]
    service_code: NotRequired[
        "capo_workspaces_thin_client.types.service_code.ServiceCode"
    ]
    """<p>The code for the service in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""
    quota_code: NotRequired["capo_workspaces_thin_client.types.quota_code.QuotaCode"]
    """<p>The code for the quota in <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a>.</p>"""
    retry_after_seconds: NotRequired[
        "capo_workspaces_thin_client.types.retry_after_seconds.RetryAfterSeconds"
    ]
    """<p>The number of seconds to wait before retrying the next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesthinclient#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ThrottlingException":
        return cls(deserialize_json(data), message)
