"""Generated from Smithy shape ``com.amazonaws.codebuild#InvalidInputException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import ServiceError

if TYPE_CHECKING:
    import capo_codebuild.types.string


class InvalidInputException_(TypedDict, closed=True):
    message: NotRequired["capo_codebuild.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInputException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codebuild#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(
        self,
        data: InvalidInputException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidInputException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
