"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceAlreadyExists``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_servicediscovery.errors import ServiceError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.error_message
    import capo_servicediscovery.types.resource_id


class ServiceAlreadyExists_(TypedDict, closed=True):
    message: NotRequired["capo_servicediscovery.types.error_message.ErrorMessage"]
    creator_request_id: NotRequired[
        "capo_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>The <code>CreatorRequestId</code> that was used to create the service.</p>"""
    service_id: NotRequired["capo_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID of the existing service.</p>"""
    service_arn: NotRequired["capo_servicediscovery.types.arn.Arn"]
    """<p>The ARN of the existing service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceAlreadyExists_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "service_id" in value:
        out["ServiceId"] = value["service_id"]
    if "service_arn" in value:
        out["ServiceArn"] = value["service_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceAlreadyExists_:
    out: ServiceAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    if data.get("ServiceArn") is not None:
        out["service_arn"] = data["ServiceArn"]
    return out


class ServiceAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicediscovery#ServiceAlreadyExists``."""

    code: str | None = "ServiceAlreadyExists"

    def __init__(
        self,
        data: ServiceAlreadyExists_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceAlreadyExists",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ServiceAlreadyExists":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
