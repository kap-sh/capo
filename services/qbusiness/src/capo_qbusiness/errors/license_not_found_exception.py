"""Generated from Smithy shape ``com.amazonaws.qbusiness#LicenseNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_qbusiness.errors import ServiceError

if TYPE_CHECKING:
    import capo_qbusiness.types.error_message


class LicenseNotFoundException_(TypedDict, closed=True):
    message: "capo_qbusiness.types.error_message.ErrorMessage"


# --- restJson1 ser/de ---
def serialize_json(value: LicenseNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LicenseNotFoundException_:
    out: LicenseNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class LicenseNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#LicenseNotFoundException``."""

    code: str | None = "LicenseNotFoundException"

    def __init__(
        self,
        data: LicenseNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LicenseNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "LicenseNotFoundException":
        return cls(deserialize_json(data), message, response=response)
