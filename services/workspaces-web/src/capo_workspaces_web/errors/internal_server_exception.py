"""Generated from Smithy shape ``com.amazonaws.workspacesweb#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import ServiceError

if TYPE_CHECKING:
    import capo_workspaces_web.types.exception_message
    import capo_workspaces_web.types.retry_after_seconds


class InternalServerException_(TypedDict, closed=True):
    message: NotRequired["capo_workspaces_web.types.exception_message.ExceptionMessage"]
    retry_after_seconds: (
        "capo_workspaces_web.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>Advice to clients on when the call can be safely retried.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workspacesweb#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_json(data), message, response=response)
