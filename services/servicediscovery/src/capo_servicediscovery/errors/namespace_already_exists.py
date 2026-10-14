"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceAlreadyExists``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import capo_servicediscovery.types.error_message
    import capo_servicediscovery.types.resource_id


class NamespaceAlreadyExists_(TypedDict, closed=True):
    message: NotRequired["capo_servicediscovery.types.error_message.ErrorMessage"]
    creator_request_id: NotRequired[
        "capo_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>The <code>CreatorRequestId</code> that was used to create the namespace.</p>"""
    namespace_id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID of the existing namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceAlreadyExists_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "namespace_id" in value:
        out["NamespaceId"] = value["namespace_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NamespaceAlreadyExists_:
    out: NamespaceAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("NamespaceId") is not None:
        out["namespace_id"] = data["NamespaceId"]
    return out


class NamespaceAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#NamespaceAlreadyExists``."""

    code: str | None = "NamespaceAlreadyExists"

    def __init__(
        self,
        data: NamespaceAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NamespaceAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "NamespaceAlreadyExists":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
