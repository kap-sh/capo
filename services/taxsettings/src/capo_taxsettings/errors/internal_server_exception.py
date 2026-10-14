"""Generated from Smithy shape ``com.amazonaws.taxsettings#InternalServerException``."""

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_taxsettings.types.error_code
    import capo_taxsettings.types.error_message


class InternalServerException_(TypedDict, closed=True):
    message: "capo_taxsettings.types.error_message.ErrorMessage"
    error_code: "capo_taxsettings.types.error_code.ErrorCode"
    """<p>500</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["errorCode"] = value["error_code"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("InternalServerException_.error_code required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_json(data), message, response=response)


def redact_sensitive(value: InternalServerException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
