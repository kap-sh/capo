"""Generated from Smithy shape ``com.amazonaws.devicefarm#ArgumentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import capo_device_farm.types.message


class ArgumentException_(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>Any additional information about the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArgumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ArgumentException_:
    out: ArgumentException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#ArgumentException``."""

    code: str | None = "ArgumentException"

    def __init__(
        self,
        data: ArgumentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ArgumentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ArgumentException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
