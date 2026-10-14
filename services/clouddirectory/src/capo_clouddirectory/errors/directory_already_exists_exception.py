"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DirectoryAlreadyExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class DirectoryAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DirectoryAlreadyExistsException_:
    out: DirectoryAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DirectoryAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#DirectoryAlreadyExistsException``."""

    code: str | None = "DirectoryAlreadyExistsException"

    def __init__(
        self,
        data: DirectoryAlreadyExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DirectoryAlreadyExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DirectoryAlreadyExistsException":
        return cls(deserialize_json(data), message, response=response)
