"""Generated from Smithy shape ``com.amazonaws.storagegateway#InternalServerError``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import ServiceError

if TYPE_CHECKING:
    import capo_storage_gateway.types.storage_gateway_error
    import capo_storage_gateway.types.string


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>A human-readable message describing the error that occurred.</p>"""
    error: NotRequired[
        "capo_storage_gateway.types.storage_gateway_error.StorageGatewayError"
    ]
    """<p>A <a>StorageGatewayError</a> that provides more information about the cause of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerError_) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
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


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.storagegateway#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(
        self,
        data: InternalServerError_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerError":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
