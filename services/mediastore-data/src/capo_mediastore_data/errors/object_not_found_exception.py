"""Generated from Smithy shape ``com.amazonaws.mediastoredata#ObjectNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediastore_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediastore_data.types.error_message


class ObjectNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_mediastore_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ObjectNotFoundException_:
    out: ObjectNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ObjectNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastoredata#ObjectNotFoundException``."""

    code: str | None = "ObjectNotFoundException"

    def __init__(
        self,
        data: ObjectNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ObjectNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ObjectNotFoundException":
        return cls(deserialize_json(data), message, response=response)
