"""Generated from Smithy shape ``com.amazonaws.s3vectors#KmsInvalidKeyUsageException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_s3vectors.types.exception_message


class KmsInvalidKeyUsageException_(TypedDict, closed=True):
    message: "capo_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: KmsInvalidKeyUsageException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KmsInvalidKeyUsageException_:
    out: KmsInvalidKeyUsageException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("KmsInvalidKeyUsageException_.message required")
    return out


class KmsInvalidKeyUsageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#KmsInvalidKeyUsageException``."""

    code: str | None = "KmsInvalidKeyUsageException"

    def __init__(
        self,
        data: KmsInvalidKeyUsageException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsInvalidKeyUsageException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KmsInvalidKeyUsageException":
        return cls(deserialize_json(data), message, response=response)
