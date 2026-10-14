"""Generated from Smithy shape ``com.amazonaws.account#ResourceUnavailableException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_account.errors import DeserializationError, ServiceError


class ResourceUnavailableException_(TypedDict, closed=True):
    message: "str"
    error_type: NotRequired["str"]
    """<p>The value populated to the <code>x-amzn-ErrorType</code> response header by API Gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceUnavailableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceUnavailableException_:
    out: ResourceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ResourceUnavailableException_.message required")
    return out


class ResourceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.account#ResourceUnavailableException``."""

    code: str | None = "ResourceUnavailableException"

    def __init__(
        self,
        data: ResourceUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceUnavailableException":
        return cls(deserialize_json(data), message, response=response)
