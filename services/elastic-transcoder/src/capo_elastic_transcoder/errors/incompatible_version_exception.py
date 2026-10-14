"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#IncompatibleVersionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_elastic_transcoder.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.exception_message


class IncompatibleVersionException_(TypedDict, closed=True):
    message: "capo_elastic_transcoder.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: IncompatibleVersionException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IncompatibleVersionException_:
    out: IncompatibleVersionException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("IncompatibleVersionException_.message required")
    return out


class IncompatibleVersionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elastictranscoder#IncompatibleVersionException``."""

    code: str | None = "IncompatibleVersionException"

    def __init__(
        self,
        data: IncompatibleVersionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncompatibleVersionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "IncompatibleVersionException":
        return cls(deserialize_json(data), message, response=response)
