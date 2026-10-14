"""Generated from Smithy shape ``com.amazonaws.route53resolver#ResourceUnavailableException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import ServiceError

if TYPE_CHECKING:
    import capo_route53resolver.types.string


class ResourceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_route53resolver.types.string.String"]
    resource_type: NotRequired["capo_route53resolver.types.string.String"]
    """<p>For a <code>ResourceUnavailableException</code> error, the type of resource that isn't available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUnavailableException_:
    out: ResourceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    return out


class ResourceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53resolver#ResourceUnavailableException``."""

    code: str | None = "ResourceUnavailableException"

    def __init__(
        self,
        data: ResourceUnavailableException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceUnavailableException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceUnavailableException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
