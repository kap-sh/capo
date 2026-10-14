"""Generated from Smithy shape ``com.amazonaws.braket#DeviceRetiredException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import ServiceError


class DeviceRetiredException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceRetiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeviceRetiredException_:
    out: DeviceRetiredException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DeviceRetiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.braket#DeviceRetiredException``."""

    code: str | None = "DeviceRetiredException"

    def __init__(
        self,
        data: DeviceRetiredException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeviceRetiredException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DeviceRetiredException":
        return cls(deserialize_json(data), message, response=response)
