"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CustomHealthNotFound``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import capo_servicediscovery.types.error_message


class CustomHealthNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_servicediscovery.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomHealthNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomHealthNotFound_:
    out: CustomHealthNotFound_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class CustomHealthNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#CustomHealthNotFound``."""

    code: str | None = "CustomHealthNotFound"

    def __init__(
        self,
        data: CustomHealthNotFound_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomHealthNotFound",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CustomHealthNotFound":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
