"""Generated from Smithy shape ``com.amazonaws.backup#InvalidResourceStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import ServiceError

if TYPE_CHECKING:
    import capo_backup.types.string


class InvalidResourceStateException_(TypedDict, closed=True):
    code: NotRequired["capo_backup.types.string.string"]
    message: NotRequired["capo_backup.types.string.string"]
    type: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""
    context: NotRequired["capo_backup.types.string.string"]
    """<p></p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidResourceStateException_) -> dict:
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


def deserialize_json(data: dict) -> InvalidResourceStateException_:
    out: InvalidResourceStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Context") is not None:
        out["context"] = data["Context"]
    return out


class InvalidResourceStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backup#InvalidResourceStateException``."""

    code: str | None = "InvalidResourceStateException"

    def __init__(
        self,
        data: InvalidResourceStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceStateException":
        return cls(deserialize_json(data), message, response=response)
