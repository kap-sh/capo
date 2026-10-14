"""Generated from Smithy shape ``com.amazonaws.devopsagent#IdentityCenterServiceException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError, ServiceError


class IdentityCenterServiceException_(TypedDict, closed=True):
    message: "str"
    """<p>Detailed error message describing why the call fails</p>"""
    underlying_error_code: NotRequired["str"]
    """<p>The Idc error code</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityCenterServiceException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "underlying_error_code" in value:
        out["underlyingErrorCode"] = value["underlying_error_code"]
    return out


def deserialize_json(data: dict) -> IdentityCenterServiceException_:
    out: IdentityCenterServiceException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("IdentityCenterServiceException_.message required")
    if data.get("underlyingErrorCode") is not None:
        out["underlying_error_code"] = data["underlyingErrorCode"]
    return out


class IdentityCenterServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devopsagent#IdentityCenterServiceException``."""

    code: str | None = "IdentityCenterServiceException"

    def __init__(
        self,
        data: IdentityCenterServiceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdentityCenterServiceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IdentityCenterServiceException":
        return cls(deserialize_json(data), message, response=response)
