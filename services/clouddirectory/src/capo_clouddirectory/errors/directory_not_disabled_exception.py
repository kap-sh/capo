"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DirectoryNotDisabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class DirectoryNotDisabledException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryNotDisabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DirectoryNotDisabledException_:
    out: DirectoryNotDisabledException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DirectoryNotDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#DirectoryNotDisabledException``."""

    code: str | None = "DirectoryNotDisabledException"

    def __init__(
        self,
        data: DirectoryNotDisabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryNotDisabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DirectoryNotDisabledException":
        return cls(deserialize_json(data), message, response=response)
