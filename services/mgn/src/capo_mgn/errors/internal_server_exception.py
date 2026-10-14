"""Generated from Smithy shape ``com.amazonaws.mgn#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_mgn.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.positive_integer


class InternalServerException_(TypedDict, closed=True):
    message: "capo_mgn.types.large_bounded_string.LargeBoundedString"
    retry_after_seconds: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>The server encountered an unexpected condition that prevented it from fulfilling the request. The request will be retried again after x seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InternalServerException_.message required")
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mgn#InternalServerException``."""

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
