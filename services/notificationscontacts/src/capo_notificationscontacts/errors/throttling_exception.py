"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_notificationscontacts.errors import ServiceError

if TYPE_CHECKING:
    import capo_notificationscontacts.types.error_message
    import capo_notificationscontacts.types.quota_code
    import capo_notificationscontacts.types.service_code


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_notificationscontacts.types.error_message.ErrorMessage"
    service_code: NotRequired[
        "capo_notificationscontacts.types.service_code.ServiceCode"
    ]
    """<p>Identifies the service being throttled.</p>"""
    quota_code: NotRequired["capo_notificationscontacts.types.quota_code.QuotaCode"]
    """<p>Identifies the quota that is being throttled.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The number of seconds a client should wait before retrying the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
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
    else:
        out["message"] = ""
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.notificationscontacts#ThrottlingException``."""

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
