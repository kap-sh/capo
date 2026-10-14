"""Generated from Smithy shape ``com.amazonaws.sfn#TooManyTags``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import ServiceError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.error_message


class TooManyTags_(TypedDict, closed=True):
    message: NotRequired["capo_sfn.types.error_message.ErrorMessage"]
    resource_name: NotRequired["capo_sfn.types.arn.Arn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TooManyTags_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TooManyTags_:
    out: TooManyTags_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


class TooManyTags(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sfn#TooManyTags``."""

    code: str | None = "TooManyTags"

    def __init__(
        self,
        data: TooManyTags_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTags",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyTags":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
