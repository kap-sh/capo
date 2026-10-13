"""Generated from Smithy shape ``com.amazonaws.appfabric#ConnectAppAuthorizationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.auth_request
    import capo_appfabric.types.identifier


class ConnectAppAuthorizationRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle that contains the app authorization to use for the request.</p>"""
    app_authorization_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>"""
    auth_request: NotRequired["capo_appfabric.types.auth_request.AuthRequest"]
    """<p>Contains OAuth2 authorization information.</p> <p>This is required if the app authorization for the request is configured with an OAuth2 (<code>oauth2</code>) authorization type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectAppAuthorizationRequest) -> dict:
    out: dict = {}
    if "auth_request" in value:
        import capo_appfabric.types.auth_request

        out["authRequest"] = capo_appfabric.types.auth_request.serialize_json(
            value["auth_request"]
        )
    return out


def deserialize_json(data: dict) -> ConnectAppAuthorizationRequest:
    out: ConnectAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("authRequest") is not None:
        import capo_appfabric.types.auth_request

        out["auth_request"] = capo_appfabric.types.auth_request.deserialize_json(
            data["authRequest"]
        )
    return out


def redact_sensitive(value: ConnectAppAuthorizationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_request" in value:
        import capo_appfabric.types.auth_request

        out["auth_request"] = capo_appfabric.types.auth_request.redact_sensitive(
            value["auth_request"]
        )
    return out
