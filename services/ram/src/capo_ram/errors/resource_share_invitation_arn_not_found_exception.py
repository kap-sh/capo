"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationArnNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_ram.types.string


class ResourceShareInvitationArnNotFoundException_(TypedDict, closed=True):
    message: "capo_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationArnNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceShareInvitationArnNotFoundException_:
    out: ResourceShareInvitationArnNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "ResourceShareInvitationArnNotFoundException_.message required"
        )
    return out


class ResourceShareInvitationArnNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#ResourceShareInvitationArnNotFoundException``."""

    code: str | None = "ResourceShareInvitationArnNotFoundException"

    def __init__(
        self,
        data: ResourceShareInvitationArnNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceShareInvitationArnNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceShareInvitationArnNotFoundException":
        return cls(deserialize_json(data), message, response=response)
