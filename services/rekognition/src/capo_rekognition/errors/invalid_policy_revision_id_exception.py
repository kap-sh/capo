"""Generated from Smithy shape ``com.amazonaws.rekognition#InvalidPolicyRevisionIdException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import ServiceError

if TYPE_CHECKING:
    import capo_rekognition.types.string


class InvalidPolicyRevisionIdException_(TypedDict, closed=True):
    message: NotRequired["capo_rekognition.types.string.String"]
    code: NotRequired["capo_rekognition.types.string.String"]
    logref: NotRequired["capo_rekognition.types.string.String"]
    """<p>A universally unique identifier (UUID) for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPolicyRevisionIdException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "logref" in value:
        out["Logref"] = value["logref"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPolicyRevisionIdException_:
    out: InvalidPolicyRevisionIdException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Logref") is not None:
        out["logref"] = data["Logref"]
    return out


class InvalidPolicyRevisionIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rekognition#InvalidPolicyRevisionIdException``."""

    code: str | None = "InvalidPolicyRevisionIdException"

    def __init__(
        self,
        data: InvalidPolicyRevisionIdException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyRevisionIdException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidPolicyRevisionIdException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
