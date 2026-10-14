"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#InvalidUsageDimensionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_metering.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_metering.types.error_message


class InvalidUsageDimensionException_(TypedDict, closed=True):
    message: NotRequired["capo_marketplace_metering.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidUsageDimensionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidUsageDimensionException_:
    out: InvalidUsageDimensionException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidUsageDimensionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplacemetering#InvalidUsageDimensionException``."""

    code: str | None = "InvalidUsageDimensionException"

    def __init__(
        self,
        data: InvalidUsageDimensionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidUsageDimensionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidUsageDimensionException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
