"""Generated from Smithy shape ``com.amazonaws.ssooidc#InvalidRequestRegionException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_sso_oidc.errors import ServiceError

if TYPE_CHECKING:
    import capo_sso_oidc.types.error
    import capo_sso_oidc.types.error_description
    import capo_sso_oidc.types.location
    import capo_sso_oidc.types.region


class InvalidRequestRegionException_(TypedDict, closed=True):
    error: NotRequired["capo_sso_oidc.types.error.Error"]
    """<p>Single error code. For this exception the value will be <code>invalid_request</code>.</p>"""
    error_description: NotRequired[
        "capo_sso_oidc.types.error_description.ErrorDescription"
    ]
    """<p>Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred.</p>"""
    endpoint: NotRequired["capo_sso_oidc.types.location.Location"]
    """<p>Indicates the IAM Identity Center endpoint which the requester may call with this token.</p>"""
    region: NotRequired["capo_sso_oidc.types.region.Region"]
    """<p>Indicates the region which the requester may call with this token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestRegionException_) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    if "error_description" in value:
        out["error_description"] = value["error_description"]
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> InvalidRequestRegionException_:
    out: InvalidRequestRegionException_ = {}  # type: ignore[typeddict-item]
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("error_description") is not None:
        out["error_description"] = data["error_description"]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out


class InvalidRequestRegionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssooidc#InvalidRequestRegionException``."""

    code: str | None = "InvalidRequestRegionException"

    def __init__(
        self,
        data: InvalidRequestRegionException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestRegionException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidRequestRegionException":
        return cls(deserialize_json(data), message, response=response)
