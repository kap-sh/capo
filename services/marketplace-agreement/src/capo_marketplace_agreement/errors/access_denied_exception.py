"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import ServiceError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.access_denied_exception_reason
    import capo_marketplace_agreement.types.exception_message
    import capo_marketplace_agreement.types.request_id


class AccessDeniedException_(TypedDict, closed=True):
    request_id: NotRequired["capo_marketplace_agreement.types.request_id.RequestId"]
    """<p>The unique identifier for the error.</p>"""
    message: NotRequired[
        "capo_marketplace_agreement.types.exception_message.ExceptionMessage"
    ]
    """<p>Description of the error.</p>"""
    reason: NotRequired[
        "capo_marketplace_agreement.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    ]
    """<p>The reason for the access denied exception.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "message" in value:
        out["message"] = value["message"]
    if "reason" in value:
        import capo_marketplace_agreement.types.access_denied_exception_reason

        out["reason"] = (
            capo_marketplace_agreement.types.access_denied_exception_reason.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("requestId") is not None:
        out["request_id"] = data["requestId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("reason") is not None:
        import capo_marketplace_agreement.types.access_denied_exception_reason

        out["reason"] = (
            capo_marketplace_agreement.types.access_denied_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.marketplaceagreement#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(
        self,
        data: AccessDeniedException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_0(data), message, response=response)
