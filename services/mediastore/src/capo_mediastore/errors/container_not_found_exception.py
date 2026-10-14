"""Generated from Smithy shape ``com.amazonaws.mediastore#ContainerNotFoundException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_mediastore.errors import ServiceError

if TYPE_CHECKING:
    import capo_mediastore.types.error_message


class ContainerNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_mediastore.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerNotFoundException_:
    out: ContainerNotFoundException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class ContainerNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastore#ContainerNotFoundException``."""

    code: str | None = "ContainerNotFoundException"

    def __init__(
        self,
        data: ContainerNotFoundException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContainerNotFoundException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ContainerNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
