"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_directory_service_data.types.access_denied_reason
    import capo_directory_service_data.types.exception_message


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_directory_service_data.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "capo_directory_service_data.types.access_denied_reason.AccessDeniedReason"
    ]
    """<p> Reason the request was unauthorized. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_directory_service_data.types.access_denied_reason

        out["Reason"] = (
            capo_directory_service_data.types.access_denied_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_directory_service_data.types.access_denied_reason

        out["reason"] = (
            capo_directory_service_data.types.access_denied_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservicedata#AccessDeniedException``."""

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
