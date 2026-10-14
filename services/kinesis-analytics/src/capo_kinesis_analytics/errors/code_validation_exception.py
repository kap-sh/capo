"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CodeValidationException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics.errors import ServiceError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.error_message


class CodeValidationException_(TypedDict, closed=True):
    message: NotRequired["capo_kinesis_analytics.types.error_message.ErrorMessage"]
    """<p>Test</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeValidationException_:
    out: CodeValidationException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class CodeValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kinesisanalytics#CodeValidationException``."""

    code: str | None = "CodeValidationException"

    def __init__(
        self,
        data: CodeValidationException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CodeValidationException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "CodeValidationException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
