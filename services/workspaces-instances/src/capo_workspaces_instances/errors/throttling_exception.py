"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ThrottlingException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces_instances.errors import DeserializationError, ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    """<p>Description of the throttling event.</p>"""
    service_code: NotRequired["str"]
    """<p>Code identifying the service experiencing throttling.</p>"""
    quota_code: NotRequired["str"]
    """<p>Specific code for the throttling quota.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>Recommended wait time before retrying the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "retry_after_seconds" in value:
        out["RetryAfterSeconds"] = value["retry_after_seconds"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("RetryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["RetryAfterSeconds"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesinstances#ThrottlingException``."""

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
            is_throttling_error=True,
            is_retryable=True,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
