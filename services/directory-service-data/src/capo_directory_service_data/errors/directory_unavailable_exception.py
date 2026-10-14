"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#DirectoryUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_directory_service_data.errors import ServiceError

if TYPE_CHECKING:
    import capo_directory_service_data.types.directory_unavailable_reason
    import capo_directory_service_data.types.exception_message


class DirectoryUnavailableException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_directory_service_data.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "capo_directory_service_data.types.directory_unavailable_reason.DirectoryUnavailableReason"
    ]
    """<p> Reason the request failed for the specified directory. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_directory_service_data.types.directory_unavailable_reason

        out["Reason"] = (
            capo_directory_service_data.types.directory_unavailable_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> DirectoryUnavailableException_:
    out: DirectoryUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_directory_service_data.types.directory_unavailable_reason

        out["reason"] = (
            capo_directory_service_data.types.directory_unavailable_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class DirectoryUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservicedata#DirectoryUnavailableException``."""

    code: str | None = "DirectoryUnavailableException"

    def __init__(
        self,
        data: DirectoryUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="DirectoryUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DirectoryUnavailableException":
        return cls(deserialize_json(data), message, response=response)
