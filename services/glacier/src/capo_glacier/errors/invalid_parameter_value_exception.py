"""Generated from Smithy shape ``com.amazonaws.glacier#InvalidParameterValueException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_glacier.errors import ServiceError

if TYPE_CHECKING:
    import capo_glacier.types.string


class InvalidParameterValueException_(TypedDict, closed=True):
    type: NotRequired["capo_glacier.types.string.string"]
    """<p>Client</p>"""
    code: NotRequired["capo_glacier.types.string.string"]
    """<p>400 Bad Request</p>"""
    message: NotRequired["capo_glacier.types.string.string"]
    """<p>Returned if a parameter of the request is incorrectly specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.glacier#InvalidParameterValueException``."""

    code: str | None = "InvalidParameterValueException"

    def __init__(
        self,
        data: InvalidParameterValueException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidParameterValueException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidParameterValueException":
        return cls(deserialize_json(data), message, response=response)
