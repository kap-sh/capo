"""Generated from Smithy shape ``com.amazonaws.s3vectors#KmsInvalidStateException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_s3vectors.errors import ServiceError

if TYPE_CHECKING:
    import capo_s3vectors.types.exception_message


class KmsInvalidStateException_(TypedDict, closed=True):
    message: "capo_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: KmsInvalidStateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KmsInvalidStateException_:
    out: KmsInvalidStateException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class KmsInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#KmsInvalidStateException``."""

    code: str | None = "KmsInvalidStateException"

    def __init__(
        self,
        data: KmsInvalidStateException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsInvalidStateException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KmsInvalidStateException":
        return cls(deserialize_json(data), message, response=response)
