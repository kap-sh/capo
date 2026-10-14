"""Generated from Smithy shape ``com.amazonaws.mpa#InvalidParameterException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_mpa.types.string


class InvalidParameterException_(TypedDict, closed=True):
    message: "capo_mpa.types.string.String"
    """<p>Message for the <code>InvalidParameterException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterException_:
    out: InvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("InvalidParameterException_.message required")
    return out


class InvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mpa#InvalidParameterException``."""

    code: str | None = "InvalidParameterException"

    def __init__(
        self,
        data: InvalidParameterException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParameterException":
        return cls(deserialize_json(data), message, response=response)
