"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_securityhub.errors import ServiceError

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class ResourceInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    code: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_json(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.securityhub#ResourceInUseException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceInUseException":
        return cls(deserialize_json(data), message, response=response)
