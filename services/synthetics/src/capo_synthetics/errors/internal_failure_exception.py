"""Generated from Smithy shape ``com.amazonaws.synthetics#InternalFailureException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_synthetics.errors import ServiceError

if TYPE_CHECKING:
    import capo_synthetics.types.error_message


class InternalFailureException_(TypedDict, closed=True):
    message: NotRequired["capo_synthetics.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: InternalFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalFailureException_:
    out: InternalFailureException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.synthetics#InternalFailureException``."""

    code: str | None = "InternalFailureException"

    def __init__(
        self,
        data: InternalFailureException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalFailureException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalFailureException":
        return cls(deserialize_json(data), message, response=response)
