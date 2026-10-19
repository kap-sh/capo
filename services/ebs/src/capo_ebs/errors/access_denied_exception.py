"""Generated from Smithy shape ``com.amazonaws.ebs#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ebs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ebs.types.access_denied_exception_reason
    import capo_ebs.types.error_message


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["capo_ebs.types.error_message.ErrorMessage"]
    reason: "capo_ebs.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    """<p>The reason for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    import capo_ebs.types.access_denied_exception_reason

    out["Reason"] = capo_ebs.types.access_denied_exception_reason.serialize_json(
        value["reason"]
    )
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_ebs.types.access_denied_exception_reason

        out["reason"] = capo_ebs.types.access_denied_exception_reason.deserialize_json(
            data["Reason"]
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_ebs.types.access_denied_exception_reason.AccessDeniedExceptionReason",
            "",
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ebs#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(
        self,
        data: AccessDeniedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDeniedException":
        return cls(deserialize_json(data), message, response=response)
