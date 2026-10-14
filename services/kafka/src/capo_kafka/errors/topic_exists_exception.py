"""Generated from Smithy shape ``com.amazonaws.kafka#TopicExistsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kafka.errors import ServiceError

if TYPE_CHECKING:
    import capo_kafka.types.__string


class TopicExistsException_(TypedDict, closed=True):
    invalid_parameter: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The parameter that caused the error.</p>"""
    message: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicExistsException_) -> dict:
    out: dict = {}
    if "invalid_parameter" in value:
        out["invalidParameter"] = value["invalid_parameter"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TopicExistsException_:
    out: TopicExistsException_ = {}  # type: ignore[typeddict-item]
    if data.get("invalidParameter") is not None:
        out["invalid_parameter"] = data["invalidParameter"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class TopicExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kafka#TopicExistsException``."""

    code: str | None = "TopicExistsException"

    def __init__(
        self,
        data: TopicExistsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TopicExistsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TopicExistsException":
        return cls(deserialize_json(data), message, response=response)
