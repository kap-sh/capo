"""Generated from Smithy shape ``com.amazonaws.efs#NoFreeAddressesInSubnet``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_efs.types.error_code
    import capo_efs.types.error_message


class NoFreeAddressesInSubnet_(TypedDict, closed=True):
    error_code: "capo_efs.types.error_code.ErrorCode"
    message: NotRequired["capo_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: NoFreeAddressesInSubnet_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NoFreeAddressesInSubnet_:
    out: NoFreeAddressesInSubnet_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("NoFreeAddressesInSubnet_.error_code required")
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class NoFreeAddressesInSubnet(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#NoFreeAddressesInSubnet``."""

    code: str | None = "NoFreeAddressesInSubnet"

    def __init__(
        self,
        data: NoFreeAddressesInSubnet_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoFreeAddressesInSubnet",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NoFreeAddressesInSubnet":
        return cls(deserialize_json(data), message, response=response)
