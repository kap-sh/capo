"""Generated from Smithy shape ``com.amazonaws.applicationinsights#InternalServerException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_application_insights.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_insights.types.error_msg


class InternalServerException_(TypedDict, closed=True):
    message: NotRequired["capo_application_insights.types.error_msg.ErrorMsg"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationinsights#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(
        self,
        data: InternalServerException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InternalServerException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
