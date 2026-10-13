"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetIdentityProviderResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.identity_provider


class GetIdentityProviderResponse(TypedDict, closed=True):
    identity_provider: NotRequired[
        "capo_workspaces_web.types.identity_provider.IdentityProvider"
    ]
    """<p>The identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityProviderResponse) -> dict:
    out: dict = {}
    if "identity_provider" in value:
        import capo_workspaces_web.types.identity_provider

        out["identityProvider"] = (
            capo_workspaces_web.types.identity_provider.serialize_json(
                value["identity_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIdentityProviderResponse:
    out: GetIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("identityProvider") is not None:
        import capo_workspaces_web.types.identity_provider

        out["identity_provider"] = (
            capo_workspaces_web.types.identity_provider.deserialize_json(
                data["identityProvider"]
            )
        )
    return out


def redact_sensitive(value: GetIdentityProviderResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "identity_provider" in value:
        import capo_workspaces_web.types.identity_provider

        out["identity_provider"] = (
            capo_workspaces_web.types.identity_provider.redact_sensitive(
                value["identity_provider"]
            )
        )
    return out
