"""Generated from Smithy shape ``com.amazonaws.greengrass#BadRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_greengrass.errors import ServiceError

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.error_details


class BadRequestException_(TypedDict, closed=True):
    error_details: NotRequired["capo_greengrass.types.error_details.ErrorDetails"]
    """Details about the error."""
    message: NotRequired["capo_greengrass.types.__string.__string"]
    """A message containing information about the error."""


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "error_details" in value:
        import capo_greengrass.types.error_details

        out["ErrorDetails"] = capo_greengrass.types.error_details.serialize_json(
            value["error_details"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorDetails") is not None:
        import capo_greengrass.types.error_details

        out["error_details"] = capo_greengrass.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.greengrass#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(
        self,
        data: BadRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BadRequestException":
        return cls(deserialize_json(data), message, response=response)
