"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ServerInternalErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_application_discovery_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_discovery_service.types.message


class ServerInternalErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_application_discovery_service.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerInternalErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServerInternalErrorException_:
    out: ServerInternalErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ServerInternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationdiscoveryservice#ServerInternalErrorException``."""

    code: str | None = "ServerInternalErrorException"

    def __init__(
        self,
        data: ServerInternalErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServerInternalErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServerInternalErrorException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
