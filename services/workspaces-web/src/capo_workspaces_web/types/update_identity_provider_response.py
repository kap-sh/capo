"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateIdentityProviderResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.identity_provider


class UpdateIdentityProviderResponse(TypedDict, closed=True):
    identity_provider: "capo_workspaces_web.types.identity_provider.IdentityProvider"
    """<p>The identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdentityProviderResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.identity_provider

    out["identityProvider"] = (
        capo_workspaces_web.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIdentityProviderResponse:
    out: UpdateIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if data.get("identityProvider") is not None:
        import capo_workspaces_web.types.identity_provider

        out["identity_provider"] = (
            capo_workspaces_web.types.identity_provider.deserialize_json(
                data["identityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateIdentityProviderResponse.identity_provider required"
        )
    return out


def redact_sensitive(value: UpdateIdentityProviderResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "identity_provider" in value:
        import capo_workspaces_web.types.identity_provider

        out["identity_provider"] = (
            capo_workspaces_web.types.identity_provider.redact_sensitive(
                value["identity_provider"]
            )
        )
    return out
