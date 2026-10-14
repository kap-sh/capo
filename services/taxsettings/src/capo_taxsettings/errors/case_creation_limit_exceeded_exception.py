"""Generated from Smithy shape ``com.amazonaws.taxsettings#CaseCreationLimitExceededException``."""

from typing import TYPE_CHECKING, Any

import zapros
from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_taxsettings.types.error_message


class CaseCreationLimitExceededException_(TypedDict, closed=True):
    message: "capo_taxsettings.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: CaseCreationLimitExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CaseCreationLimitExceededException_:
    out: CaseCreationLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "CaseCreationLimitExceededException_.message required"
        )
    return out


class CaseCreationLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#CaseCreationLimitExceededException``."""

    code: str | None = "CaseCreationLimitExceededException"

    def __init__(
        self,
        data: CaseCreationLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CaseCreationLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CaseCreationLimitExceededException":
        return cls(deserialize_json(data), message, response=response)


def redact_sensitive(value: CaseCreationLimitExceededException_) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
