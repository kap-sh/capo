"""Generated from Smithy shape ``com.amazonaws.drs#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_drs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_drs.types.large_bounded_string


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_drs.types.large_bounded_string.LargeBoundedString"
    service_code: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Service code.</p>"""
    quota_code: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Quota code.</p>"""
    retry_after_seconds: NotRequired[
        "capo_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>The number of seconds after which the request should be safe to retry.</p>"""


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
        raise DeserializationError("ThrottlingException_.message required")
    if data.get("serviceCode") is not None:
        out["service_code"] = data["serviceCode"]
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.drs#ThrottlingException``."""

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
