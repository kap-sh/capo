"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_connectscheduling.errors import ServiceError

if TYPE_CHECKING:
    import capo_connectscheduling.types.message


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_connectscheduling.types.message.Message"
    quota_code: NotRequired["str"]
    """<p>The code of the quota that was throttled, for use with the Service Quotas API.</p>"""
    service_code: NotRequired["str"]
    """<p>The code of the service that owns the quota.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds to wait before retrying.</p>"""


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
        out["message"] = ""
    if data.get("QuotaCode") is not None:
        out["quota_code"] = data["QuotaCode"]
    if data.get("ServiceCode") is not None:
        out["service_code"] = data["ServiceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectscheduling#ThrottlingException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)
