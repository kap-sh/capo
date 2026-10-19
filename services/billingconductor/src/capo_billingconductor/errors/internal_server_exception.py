"""Generated from Smithy shape ``com.amazonaws.billingconductor#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_billingconductor.errors import ServiceError

if TYPE_CHECKING:
    import capo_billingconductor.types.retry_after_seconds
    import capo_billingconductor.types.string


class InternalServerException_(TypedDict, closed=True):
    message: "capo_billingconductor.types.string.String"
    retry_after_seconds: (
        "capo_billingconductor.types.retry_after_seconds.RetryAfterSeconds"
    )
    """<p>Number of seconds you can retry after the call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billingconductor#InternalServerException``."""

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
