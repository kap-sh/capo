"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ThrottlingException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import ServiceError

if TYPE_CHECKING:
    import capo_resiliencehub.types.retry_after_seconds
    import capo_resiliencehub.types.string500


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired["capo_resiliencehub.types.string500.String500"]
    retry_after_seconds: NotRequired[
        "capo_resiliencehub.types.retry_after_seconds.RetryAfterSeconds"
    ]
    """<p>The number of seconds to wait before retrying the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "retry_after_seconds" in value:
        out["retryAfterSeconds"] = value["retry_after_seconds"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("retryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["retryAfterSeconds"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.resiliencehub#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(
        self,
        data: ThrottlingException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ThrottlingException":
        return cls(deserialize_json(data), message, response=response)
