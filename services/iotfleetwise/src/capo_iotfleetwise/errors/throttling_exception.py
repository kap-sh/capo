"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.retry_after_seconds
    import capo_iotfleetwise.types.string


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_iotfleetwise.types.string.string"
    quota_code: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>The quota identifier of the applied throttling rules for this request.</p>"""
    service_code: NotRequired["capo_iotfleetwise.types.string.string"]
    """<p>The code for the service that couldn't be completed due to throttling.</p>"""
    retry_after_seconds: "capo_iotfleetwise.types.retry_after_seconds.RetryAfterSeconds"
    """<p>The number of seconds to wait before retrying the command.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "quota_code" in value:
        out["quotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["serviceCode"] = value["service_code"]
    out["retryAfterSeconds"] = value.get("retry_after_seconds", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("retryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["retryAfterSeconds"]
    else:
        out["retry_after_seconds"] = 0
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#ThrottlingException``."""

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
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
