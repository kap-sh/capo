"""Generated from Smithy shape ``com.amazonaws.kafka#NotControllerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kafka.errors import ServiceError

if TYPE_CHECKING:
    import capo_kafka.types.__string


class NotControllerException_(TypedDict, closed=True):
    invalid_parameter: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The parameter that caused the error.</p>"""
    message: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotControllerException_) -> dict:
    out: dict = {}
    if "invalid_parameter" in value:
        out["invalidParameter"] = value["invalid_parameter"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotControllerException_:
    out: NotControllerException_ = {}  # type: ignore[typeddict-item]
    if data.get("invalidParameter") is not None:
        out["invalid_parameter"] = data["invalidParameter"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class NotControllerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kafka#NotControllerException``."""

    code: str | None = "NotControllerException"

    def __init__(
        self,
        data: NotControllerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotControllerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotControllerException":
        return cls(deserialize_json(data), message, response=response)
