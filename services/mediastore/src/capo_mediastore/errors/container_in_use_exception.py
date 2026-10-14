"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediastore.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediastore.types.error_message


class ContainerInUseException_(TypedDict, closed=True):
    message: NotRequired["capo_mediastore.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInUseException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerInUseException_:
    out: ContainerInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ContainerInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastore#ContainerInUseException``."""

    code: str | None = "ContainerInUseException"

    def __init__(
        self,
        data: ContainerInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContainerInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ContainerInUseException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
