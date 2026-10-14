"""Generated from Smithy shape ``com.amazonaws.greengrass#InternalServerErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_greengrass.errors import ServiceError

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.error_details


class InternalServerErrorException_(TypedDict, closed=True):
    error_details: NotRequired["capo_greengrass.types.error_details.ErrorDetails"]
    """Details about the error."""
    message: NotRequired["capo_greengrass.types.__string.__string"]
    """A message containing information about the error."""


# --- restJson1 ser/de ---
def serialize_json(value: InternalServerErrorException_) -> dict:
    out: dict = {}
    if "error_details" in value:
        import capo_greengrass.types.error_details

        out["ErrorDetails"] = capo_greengrass.types.error_details.serialize_json(
            value["error_details"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InternalServerErrorException_:
    out: InternalServerErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("ErrorDetails") is not None:
        import capo_greengrass.types.error_details

        out["error_details"] = capo_greengrass.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServerErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.greengrass#InternalServerErrorException``."""

    code: str | None = "InternalServerErrorException"

    def __init__(
        self,
        data: InternalServerErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerErrorException":
        return cls(deserialize_json(data), message, response=response)
