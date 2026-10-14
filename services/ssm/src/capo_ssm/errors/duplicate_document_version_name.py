"""Generated from Smithy shape ``com.amazonaws.ssm#DuplicateDocumentVersionName``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class DuplicateDocumentVersionName_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateDocumentVersionName_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateDocumentVersionName_:
    out: DuplicateDocumentVersionName_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class DuplicateDocumentVersionName(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#DuplicateDocumentVersionName``."""

    code: str | None = "DuplicateDocumentVersionName"

    def __init__(
        self,
        data: DuplicateDocumentVersionName_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateDocumentVersionName",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateDocumentVersionName":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
