"""Generated from Smithy shape ``com.amazonaws.snowball#InvalidResourceException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_snowball.errors import ServiceError

if TYPE_CHECKING:
    import capo_snowball.types.string


class InvalidResourceException_(TypedDict, closed=True):
    message: NotRequired["capo_snowball.types.string.String"]
    resource_type: NotRequired["capo_snowball.types.string.String"]
    """<p>The provided resource value is invalid.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidResourceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidResourceException_:
    out: InvalidResourceException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class InvalidResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.snowball#InvalidResourceException``."""

    code: str | None = "InvalidResourceException"

    def __init__(
        self,
        data: InvalidResourceException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
