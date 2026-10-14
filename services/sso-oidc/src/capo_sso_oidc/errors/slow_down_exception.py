"""Generated from Smithy shape ``com.amazonaws.ssooidc#SlowDownException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sso_oidc.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_oidc.types.error
    import capo_sso_oidc.types.error_description


class SlowDownException_(TypedDict, closed=True):
    error: NotRequired["capo_sso_oidc.types.error.Error"]
    """<p>Single error code. For this exception the value will be <code>slow_down</code>.</p>"""
    error_description: NotRequired[
        "capo_sso_oidc.types.error_description.ErrorDescription"
    ]
    """<p>Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlowDownException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "error_description" in value:
        out["error_description"] = value["error_description"]
    return out


def deserialize_json(data: dict) -> SlowDownException_:
    out: SlowDownException_ = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("error_description") is not None:
        out["error_description"] = data["error_description"]
    return out


class SlowDownException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssooidc#SlowDownException``."""

    code: str | None = "SlowDownException"

    def __init__(
        self,
        data: SlowDownException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SlowDownException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "SlowDownException":
        return cls(deserialize_json(data), message, response=response)
