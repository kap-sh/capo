"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.access_denied_exception_error_code


class AccessDeniedException_(TypedDict, closed=True):
    message: NotRequired["str"]
    reason: NotRequired[
        "capo_partnercentral_selling.types.access_denied_exception_error_code.AccessDeniedExceptionErrorCode"
    ]
    """<p>The reason why access was denied for the requested operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import capo_partnercentral_selling.types.access_denied_exception_error_code

        out["Reason"] = (
            capo_partnercentral_selling.types.access_denied_exception_error_code.serialize_aws_json_1_0(
                value["reason"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Reason") is not None:
        import capo_partnercentral_selling.types.access_denied_exception_error_code

        out["reason"] = (
            capo_partnercentral_selling.types.access_denied_exception_error_code.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralselling#AccessDeniedException``."""

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
