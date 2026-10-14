"""Generated from Smithy shape ``com.amazonaws.route53domains#DuplicateRequest``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53_domains.types.error_message
    import capo_route_53_domains.types.request_id


class DuplicateRequest_(TypedDict, closed=True):
    request_id: NotRequired["capo_route_53_domains.types.request_id.RequestId"]
    """<p>ID of the request operation.</p>"""
    message: NotRequired["capo_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The request is already in progress for the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DuplicateRequest_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DuplicateRequest_:
    out: DuplicateRequest_ = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class DuplicateRequest(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#DuplicateRequest``."""

    code: str | None = "DuplicateRequest"

    def __init__(
        self,
        data: DuplicateRequest_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateRequest",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "DuplicateRequest":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
