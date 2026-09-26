"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ThrottlingException``."""

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired["str"]
    service_code: NotRequired["str"]
    """<p>The service code of the throttled service quota.</p>"""
    quota_code: NotRequired["str"]
    """<p>The quota code of the throttled service quota.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying the request.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.lambdamicrovms#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ThrottlingException":
        return cls(deserialize_json(data), message)
