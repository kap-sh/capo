"""Generated from Smithy shape ``com.amazonaws.clouddirectory#IndexedAttributeMissingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class IndexedAttributeMissingException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: IndexedAttributeMissingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IndexedAttributeMissingException_:
    out: IndexedAttributeMissingException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class IndexedAttributeMissingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#IndexedAttributeMissingException``."""

    code: str | None = "IndexedAttributeMissingException"

    def __init__(
        self,
        data: IndexedAttributeMissingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IndexedAttributeMissingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IndexedAttributeMissingException":
        return cls(deserialize_json(data), message, response=response)
