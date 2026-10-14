"""Generated from Smithy shape ``com.amazonaws.appintegrations#ResourceQuotaExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_appintegrations.errors import ServiceError

if TYPE_CHECKING:
    import capo_appintegrations.types.message


class ResourceQuotaExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_appintegrations.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceQuotaExceededException_:
    out: ResourceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appintegrations#ResourceQuotaExceededException``."""

    code: str | None = "ResourceQuotaExceededException"

    def __init__(
        self,
        data: ResourceQuotaExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceQuotaExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceQuotaExceededException":
        return cls(deserialize_json(data), message, response=response)
