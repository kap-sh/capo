"""Generated from Smithy shape ``com.amazonaws.applicationinsights#TagsAlreadyExistException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_application_insights.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_insights.types.exception_message


class TagsAlreadyExistException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_application_insights.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagsAlreadyExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TagsAlreadyExistException_:
    out: TagsAlreadyExistException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class TagsAlreadyExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationinsights#TagsAlreadyExistException``."""

    code: str | None = "TagsAlreadyExistException"

    def __init__(
        self,
        data: TagsAlreadyExistException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TagsAlreadyExistException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TagsAlreadyExistException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
