"""Generated from Smithy shape ``com.amazonaws.storagegateway#InvalidGatewayRequestException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import ServiceError

if TYPE_CHECKING:
    import capo_storage_gateway.types.storage_gateway_error
    import capo_storage_gateway.types.string


class InvalidGatewayRequestException_(TypedDict, closed=True):
    message: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>A human-readable message describing the error that occurred.</p>"""
    error: NotRequired[
        "capo_storage_gateway.types.storage_gateway_error.StorageGatewayError"
    ]
    """<p>A <a>StorageGatewayError</a> that provides more detail about the cause of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidGatewayRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "error" in value:
        import capo_storage_gateway.types.storage_gateway_error

        out["error"] = (
            capo_storage_gateway.types.storage_gateway_error.serialize_aws_json_1_1(
                value["error"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidGatewayRequestException_:
    out: InvalidGatewayRequestException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("error") is not None:
        import capo_storage_gateway.types.storage_gateway_error

        out["error"] = (
            capo_storage_gateway.types.storage_gateway_error.deserialize_aws_json_1_1(
                data["error"]
            )
        )
    return out


class InvalidGatewayRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.storagegateway#InvalidGatewayRequestException``."""

    code: str | None = "InvalidGatewayRequestException"

    def __init__(
        self,
        data: InvalidGatewayRequestException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidGatewayRequestException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidGatewayRequestException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
