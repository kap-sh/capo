"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import TypedDict

from capo_partnercentral_account.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.access_denied_exception_reason


class AccessDeniedException_(TypedDict, closed=True):
    message: "str"
    reason: "capo_partnercentral_account.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    """<p>The specific reason for the access denial.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_account.types.access_denied_exception_reason

    out["Reason"] = (
        capo_partnercentral_account.types.access_denied_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Reason") is not None:
        import capo_partnercentral_account.types.access_denied_exception_reason

        out["reason"] = (
            capo_partnercentral_account.types.access_denied_exception_reason.deserialize_aws_json_1_0(
                data["Reason"]
            )
        )
    else:
        import typing

        out["reason"] = typing.cast(
            "capo_partnercentral_account.types.access_denied_exception_reason.AccessDeniedExceptionReason",
            "",
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralaccount#AccessDeniedException``."""

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
