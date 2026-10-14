"""Generated from Smithy shape ``com.amazonaws.ecr#EmptyUploadException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message


class EmptyUploadException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]
    """<p>The error message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmptyUploadException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmptyUploadException_:
    out: EmptyUploadException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class EmptyUploadException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#EmptyUploadException``."""

    code: str | None = "EmptyUploadException"

    def __init__(
        self,
        data: EmptyUploadException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EmptyUploadException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "EmptyUploadException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
