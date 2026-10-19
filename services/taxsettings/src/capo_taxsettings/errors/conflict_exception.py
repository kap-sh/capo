"""Generated from Smithy shape ``com.amazonaws.taxsettings#ConflictException``."""

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import TypedDict

from capo_taxsettings.errors import ServiceError

if TYPE_CHECKING:
    import capo_taxsettings.types.error_code
    import capo_taxsettings.types.error_message


class ConflictException_(TypedDict, closed=True):
    message: "capo_taxsettings.types.error_message.ErrorMessage"
    error_code: "capo_taxsettings.types.error_code.ErrorCode"
    """<p>409</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["errorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)


def redact_sensitive(value: ConflictException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
