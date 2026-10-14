"""Generated from Smithy shape ``com.amazonaws.translate#TextSizeLimitExceededException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import ServiceError

if TYPE_CHECKING:
    import capo_translate.types.string


class TextSizeLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_translate.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextSizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TextSizeLimitExceededException_:
    out: TextSizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TextSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#TextSizeLimitExceededException``."""

    code: str | None = "TextSizeLimitExceededException"

    def __init__(
        self,
        data: TextSizeLimitExceededException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TextSizeLimitExceededException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TextSizeLimitExceededException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
