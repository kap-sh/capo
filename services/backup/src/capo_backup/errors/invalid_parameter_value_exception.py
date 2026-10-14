"""Generated from Smithy shape ``com.amazonaws.backup#InvalidParameterValueException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import ServiceError

if TYPE_CHECKING:
    import capo_backup.types.string


class InvalidParameterValueException_(TypedDict, closed=True):
    code: NotRequired["capo_backup.types.string.string"]
    message: NotRequired["capo_backup.types.string.string"]
    type: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""
    context: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidParameterValueException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    if "type" in value:
        out["Type"] = value["type"]
    if "context" in value:
        out["Context"] = value["context"]
    return out


def deserialize_json(data: dict) -> InvalidParameterValueException_:
    out: InvalidParameterValueException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Context") is not None:
        out["context"] = data["Context"]
    return out


class InvalidParameterValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backup#InvalidParameterValueException``."""

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
