"""Generated from Smithy shape ``com.amazonaws.transfer#InvalidNextTokenException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_transfer.errors import ServiceError

if TYPE_CHECKING:
    import capo_transfer.types.message


class InvalidNextTokenException_(TypedDict, closed=True):
    message: "capo_transfer.types.message.Message"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidNextTokenException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidNextTokenException_:
    out: InvalidNextTokenException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out


class InvalidNextTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.transfer#InvalidNextTokenException``."""

    code: str | None = "InvalidNextTokenException"

    def __init__(
        self,
        data: InvalidNextTokenException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextTokenException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidNextTokenException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
