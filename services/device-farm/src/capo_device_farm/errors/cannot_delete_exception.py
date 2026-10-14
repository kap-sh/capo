"""Generated from Smithy shape ``com.amazonaws.devicefarm#CannotDeleteException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import capo_device_farm.types.message


class CannotDeleteException_(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CannotDeleteException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CannotDeleteException_:
    out: CannotDeleteException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CannotDeleteException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#CannotDeleteException``."""

    code: str | None = "CannotDeleteException"

    def __init__(
        self,
        data: CannotDeleteException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CannotDeleteException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CannotDeleteException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
