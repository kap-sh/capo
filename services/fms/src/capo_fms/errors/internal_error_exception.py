"""Generated from Smithy shape ``com.amazonaws.fms#InternalErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import ServiceError

if TYPE_CHECKING:
    import capo_fms.types.error_message


class InternalErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_fms.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalErrorException_:
    out: InternalErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fms#InternalErrorException``."""

    code: str | None = "InternalErrorException"

    def __init__(
        self,
        data: InternalErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalErrorException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
