"""Generated from Smithy shape ``com.amazonaws.rbin#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rbin.errors import ServiceError

if TYPE_CHECKING:
    import capo_rbin.types.conflict_exception_reason
    import capo_rbin.types.error_message


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["capo_rbin.types.error_message.ErrorMessage"]
    reason: NotRequired[
        "capo_rbin.types.conflict_exception_reason.ConflictExceptionReason"
    ]
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_rbin.types.conflict_exception_reason

        out["Reason"] = capo_rbin.types.conflict_exception_reason.serialize_json(
            value["reason"]
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_rbin.types.conflict_exception_reason

        out["reason"] = capo_rbin.types.conflict_exception_reason.deserialize_json(
            data["Reason"]
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rbin#ConflictException``."""

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
