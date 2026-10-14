"""Generated from Smithy shape ``com.amazonaws.medicalimaging#NotAcceptableException``."""

import zapros
from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError, ServiceError


class NotAcceptableException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NotAcceptableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotAcceptableException_:
    out: NotAcceptableException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotAcceptableException_.message required")
    return out


class NotAcceptableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.medicalimaging#NotAcceptableException``."""

    code: str | None = "NotAcceptableException"

    def __init__(
        self,
        data: NotAcceptableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotAcceptableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NotAcceptableException":
        return cls(deserialize_json(data), message, response=response)
