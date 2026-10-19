"""Generated from Smithy shape ``com.amazonaws.grafana#ThrottlingException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_grafana.errors import ServiceError


class ThrottlingException_(TypedDict, closed=True):
    message: "str"
    """<p>A description of the error.</p>"""
    service_code: NotRequired["str"]
    """<p>The ID of the service that is associated with the error.</p>"""
    quota_code: NotRequired["str"]
    """<p>The ID of the service quota that was exceeded.</p>"""
    retry_after_seconds: NotRequired["int"]
    """<p>The value of a parameter in the request caused an error.</p>"""


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
    """Modeled error for Smithy shape ``com.amazonaws.grafana#ThrottlingException``."""

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
