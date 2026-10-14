"""Generated from Smithy shape ``com.amazonaws.novaact#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_nova_act.types.non_blank_string


class AccessDeniedException_(TypedDict, closed=True):
    message: "capo_nova_act.types.non_blank_string.NonBlankString"
    """<p>You don't have sufficient permissions to perform this action. Verify your IAM permissions and try again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.novaact#AccessDeniedException``."""

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
