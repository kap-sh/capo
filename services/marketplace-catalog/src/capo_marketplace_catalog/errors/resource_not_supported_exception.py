"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResourceNotSupportedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_catalog.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.exception_message_content


class ResourceNotSupportedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_marketplace_catalog.types.exception_message_content.ExceptionMessageContent"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNotSupportedException_:
    out: ResourceNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacecatalog#ResourceNotSupportedException``."""

    code: str | None = "ResourceNotSupportedException"

    def __init__(
        self,
        data: ResourceNotSupportedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNotSupportedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceNotSupportedException":
        return cls(deserialize_json(data), message, response=response)
