"""Generated from Smithy shape ``com.amazonaws.braket#DeviceOfflineException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import ServiceError


class DeviceOfflineException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceOfflineException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeviceOfflineException_:
    out: DeviceOfflineException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DeviceOfflineException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.braket#DeviceOfflineException``."""

    code: str | None = "DeviceOfflineException"

    def __init__(
        self,
        data: DeviceOfflineException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeviceOfflineException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DeviceOfflineException":
        return cls(deserialize_json(data), message, response=response)
