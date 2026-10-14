"""Generated from Smithy shape ``com.amazonaws.cloudtrail#InvalidMaxResultsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import capo_cloudtrail.types.error_message


class InvalidMaxResultsException_(TypedDict, closed=True):
    message: NotRequired["capo_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidMaxResultsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidMaxResultsException_:
    out: InvalidMaxResultsException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InvalidMaxResultsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#InvalidMaxResultsException``."""

    code: str | None = "InvalidMaxResultsException"

    def __init__(
        self,
        data: InvalidMaxResultsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidMaxResultsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidMaxResultsException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
