"""Generated from Smithy shape ``com.amazonaws.bedrock#TooManyTagsException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock.types.non_blank_string
    import capo_bedrock.types.taggable_resources_arn


class TooManyTagsException_(TypedDict, closed=True):
    message: NotRequired["capo_bedrock.types.non_blank_string.NonBlankString"]
    resource_name: NotRequired[
        "capo_bedrock.types.taggable_resources_arn.TaggableResourcesArn"
    ]
    """<p>The name of the resource with too many tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooManyTagsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> TooManyTagsException_:
    out: TooManyTagsException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


class TooManyTagsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrock#TooManyTagsException``."""

    code: str | None = "TooManyTagsException"

    def __init__(
        self,
        data: TooManyTagsException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTagsException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "TooManyTagsException":
        return cls(deserialize_json(data), message, response=response)
