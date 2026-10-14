"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#ResourceInUseException``."""

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_eventbridgev2.errors import ServiceError


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eventbridgev2#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(
        self,
        data: ResourceInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceInUseException":
        return cls(deserialize_cbor(data), message, response=response)
