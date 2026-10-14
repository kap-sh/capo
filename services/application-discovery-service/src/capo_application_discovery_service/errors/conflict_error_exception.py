"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ConflictErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_application_discovery_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_discovery_service.types.message


class ConflictErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_application_discovery_service.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictErrorException_:
    out: ConflictErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ConflictErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationdiscoveryservice#ConflictErrorException``."""

    code: str | None = "ConflictErrorException"

    def __init__(
        self,
        data: ConflictErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictErrorException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
