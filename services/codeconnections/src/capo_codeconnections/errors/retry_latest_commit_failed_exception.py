"""Generated from Smithy shape ``com.amazonaws.codeconnections#RetryLatestCommitFailedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_codeconnections.errors import ServiceError

if TYPE_CHECKING:
    import capo_codeconnections.types.error_message


class RetryLatestCommitFailedException_(TypedDict, closed=True):
    message: NotRequired["capo_codeconnections.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetryLatestCommitFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RetryLatestCommitFailedException_:
    out: RetryLatestCommitFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class RetryLatestCommitFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeconnections#RetryLatestCommitFailedException``."""

    code: str | None = "RetryLatestCommitFailedException"

    def __init__(
        self,
        data: RetryLatestCommitFailedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="RetryLatestCommitFailedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "RetryLatestCommitFailedException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
