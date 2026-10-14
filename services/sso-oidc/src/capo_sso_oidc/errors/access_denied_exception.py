"""Generated from Smithy shape ``com.amazonaws.ssooidc#AccessDeniedException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sso_oidc.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_oidc.types.access_denied_exception_reason
    import capo_sso_oidc.types.error
    import capo_sso_oidc.types.error_description


class AccessDeniedException_(TypedDict, closed=True):
    error: NotRequired["capo_sso_oidc.types.error.Error"]
    """<p>Single error code. For this exception the value will be <code>access_denied</code>.</p>"""
    reason: NotRequired[
        "capo_sso_oidc.types.access_denied_exception_reason.AccessDeniedExceptionReason"
    ]
    """<p>A string that uniquely identifies a reason for the error.</p>"""
    error_description: NotRequired[
        "capo_sso_oidc.types.error_description.ErrorDescription"
    ]
    """<p>Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "reason" in value:
        import capo_sso_oidc.types.access_denied_exception_reason

        out["reason"] = (
            capo_sso_oidc.types.access_denied_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "error_description" in value:
        out["error_description"] = value["error_description"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("reason") is not None:
        import capo_sso_oidc.types.access_denied_exception_reason

        out["reason"] = (
            capo_sso_oidc.types.access_denied_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    if data.get("error_description") is not None:
        out["error_description"] = data["error_description"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssooidc#AccessDeniedException``."""

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
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "AccessDeniedException":
        return cls(deserialize_json(data), message, response=response)
