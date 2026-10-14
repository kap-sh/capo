"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelErrorException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.non_blank_string
    import capo_bedrock_runtime.types.status_code


class ModelErrorException_(TypedDict, closed=True):
    message: NotRequired["capo_bedrock_runtime.types.non_blank_string.NonBlankString"]
    original_status_code: NotRequired[
        "capo_bedrock_runtime.types.status_code.StatusCode"
    ]
    """<p>The original status code.</p>"""
    resource_name: NotRequired[
        "capo_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]
    """<p>The resource name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "original_status_code" in value:
        out["originalStatusCode"] = value["original_status_code"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> ModelErrorException_:
    out: ModelErrorException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("originalStatusCode") is not None:
        out["original_status_code"] = data["originalStatusCode"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


class ModelErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ModelErrorException``."""

    code: str | None = "ModelErrorException"

    def __init__(
        self,
        data: ModelErrorException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelErrorException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ModelErrorException":
        return cls(deserialize_json(data), message, response=response)
