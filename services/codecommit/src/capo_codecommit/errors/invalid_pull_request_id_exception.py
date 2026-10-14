"""Generated from Smithy shape ``com.amazonaws.codecommit#InvalidPullRequestIdException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class InvalidPullRequestIdException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPullRequestIdException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPullRequestIdException_:
    out: InvalidPullRequestIdException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class InvalidPullRequestIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#InvalidPullRequestIdException``."""

    code: str | None = "InvalidPullRequestIdException"

    def __init__(
        self,
        data: InvalidPullRequestIdException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPullRequestIdException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPullRequestIdException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
