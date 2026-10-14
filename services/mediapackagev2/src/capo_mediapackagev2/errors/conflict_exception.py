"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.conflict_exception_type


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["str"]
    conflict_exception_type: NotRequired[
        "capo_mediapackagev2.types.conflict_exception_type.ConflictExceptionType"
    ]
    """<p>The type of ConflictException.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "conflict_exception_type" in value:
        import capo_mediapackagev2.types.conflict_exception_type

        out["ConflictExceptionType"] = (
            capo_mediapackagev2.types.conflict_exception_type.serialize_json(
                value["conflict_exception_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ConflictExceptionType") is not None:
        import capo_mediapackagev2.types.conflict_exception_type

        out["conflict_exception_type"] = (
            capo_mediapackagev2.types.conflict_exception_type.deserialize_json(
                data["ConflictExceptionType"]
            )
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediapackagev2#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_json(data), message, response=response)
