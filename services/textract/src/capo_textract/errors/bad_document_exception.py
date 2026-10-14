"""Generated from Smithy shape ``com.amazonaws.textract#BadDocumentException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_textract.errors import ServiceError

if TYPE_CHECKING:
    import capo_textract.types.string


class BadDocumentException_(TypedDict, closed=True):
    message: NotRequired["capo_textract.types.string.String"]
    code: NotRequired["capo_textract.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BadDocumentException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BadDocumentException_:
    out: BadDocumentException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    return out


class BadDocumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.textract#BadDocumentException``."""

    code: str | None = "BadDocumentException"

    def __init__(
        self,
        data: BadDocumentException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadDocumentException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "BadDocumentException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
