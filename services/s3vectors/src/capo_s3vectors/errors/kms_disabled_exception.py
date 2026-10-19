"""Generated from Smithy shape ``com.amazonaws.s3vectors#KmsDisabledException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_s3vectors.errors import ServiceError

if TYPE_CHECKING:
    import capo_s3vectors.types.exception_message


class KmsDisabledException_(TypedDict, closed=True):
    message: "capo_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: KmsDisabledException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KmsDisabledException_:
    out: KmsDisabledException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out


class KmsDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#KmsDisabledException``."""

    code: str | None = "KmsDisabledException"

    def __init__(
        self,
        data: KmsDisabledException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsDisabledException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "KmsDisabledException":
        return cls(deserialize_json(data), message, response=response)
