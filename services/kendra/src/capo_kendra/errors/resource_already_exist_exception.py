"""Generated from Smithy shape ``com.amazonaws.kendra#ResourceAlreadyExistException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import ServiceError

if TYPE_CHECKING:
    import capo_kendra.types.error_message


class ResourceAlreadyExistException_(TypedDict, closed=True):
    message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAlreadyExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAlreadyExistException_:
    out: ResourceAlreadyExistException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ResourceAlreadyExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kendra#ResourceAlreadyExistException``."""

    code: str | None = "ResourceAlreadyExistException"

    def __init__(
        self,
        data: ResourceAlreadyExistException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceAlreadyExistException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
