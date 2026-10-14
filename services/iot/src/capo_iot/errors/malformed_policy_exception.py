"""Generated from Smithy shape ``com.amazonaws.iot#MalformedPolicyException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import ServiceError

if TYPE_CHECKING:
    import capo_iot.types.error_message2


class MalformedPolicyException_(TypedDict, closed=True):
    message: NotRequired["capo_iot.types.error_message2.ErrorMessage2"]
    """<p>The message for the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MalformedPolicyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MalformedPolicyException_:
    out: MalformedPolicyException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class MalformedPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iot#MalformedPolicyException``."""

    code: str | None = "MalformedPolicyException"

    def __init__(
        self,
        data: MalformedPolicyException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedPolicyException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "MalformedPolicyException":
        return cls(deserialize_json(data), message, response=response)
