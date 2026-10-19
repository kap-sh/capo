"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ssm_incidents.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.exception_message
    import capo_ssm_incidents.types.service_code


class ThrottlingException_(TypedDict, closed=True):
    message: "capo_ssm_incidents.types.exception_message.ExceptionMessage"
    service_code: "capo_ssm_incidents.types.service_code.ServiceCode"
    """Originating service code"""
    quota_code: "str"
    """Originating quota code"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["serviceCode"] = value["service_code"]
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
    else:
        out["service_code"] = ""
    if data.get("quotaCode") is not None:
        out["quota_code"] = data["quotaCode"]
    else:
        out["quota_code"] = ""
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmincidents#ThrottlingException``."""

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
