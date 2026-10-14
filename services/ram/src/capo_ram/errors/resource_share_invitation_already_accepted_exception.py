"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationAlreadyAcceptedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class ResourceShareInvitationAlreadyAcceptedException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationAlreadyAcceptedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceShareInvitationAlreadyAcceptedException_:
    out: ResourceShareInvitationAlreadyAcceptedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "ResourceShareInvitationAlreadyAcceptedException_.message required"
        )
    return out


class ResourceShareInvitationAlreadyAcceptedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ResourceShareInvitationAlreadyAcceptedException``."""

    code: str | None = "ResourceShareInvitationAlreadyAcceptedException"

    def __init__(
        self,
        data: ResourceShareInvitationAlreadyAcceptedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceShareInvitationAlreadyAcceptedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceShareInvitationAlreadyAcceptedException":
        return cls(deserialize_json(data), message, response=response)
