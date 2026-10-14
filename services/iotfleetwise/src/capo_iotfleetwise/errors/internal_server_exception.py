"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.retry_after_seconds
    import capo_iotfleetwise.types.string


class InternalServerException_(TypedDict, closed=True):
    message: "capo_iotfleetwise.types.string.string"
    retry_after_seconds: "capo_iotfleetwise.types.retry_after_seconds.RetryAfterSeconds"
    """<p>The number of seconds to wait before retrying the command.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["retryAfterSeconds"] = value.get("retry_after_seconds", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    if data.get("retryAfterSeconds") is not None:
        out["retry_after_seconds"] = data["retryAfterSeconds"]
    else:
        out["retry_after_seconds"] = 0
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotfleetwise#InternalServerException``."""

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
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
