"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IdentityProviderSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.identity_provider_name
    import capo_workspaces_web.types.identity_provider_type
    import capo_workspaces_web.types.subresource_arn


class IdentityProviderSummary(TypedDict, closed=True):
    identity_provider_arn: "capo_workspaces_web.types.subresource_arn.SubresourceARN"
    """<p>The ARN of the identity provider.</p>"""
    identity_provider_name: NotRequired[
        "capo_workspaces_web.types.identity_provider_name.IdentityProviderName"
    ]
    """<p>The identity provider name.</p>"""
    identity_provider_type: NotRequired[
        "capo_workspaces_web.types.identity_provider_type.IdentityProviderType"
    ]
    """<p>The identity provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderSummary) -> dict:
    out: dict = {}
    out["identityProviderArn"] = value["identity_provider_arn"]
    if "identity_provider_name" in value:
        out["identityProviderName"] = value["identity_provider_name"]
    if "identity_provider_type" in value:
        out["identityProviderType"] = value["identity_provider_type"]
    return out


def deserialize_json(data: dict) -> IdentityProviderSummary:
    out: IdentityProviderSummary = {}  # type: ignore[typeddict-item]
    if data.get("identityProviderArn") is not None:
        out["identity_provider_arn"] = data["identityProviderArn"]
    else:
        raise DeserializationError(
            "IdentityProviderSummary.identity_provider_arn required"
        )
    if data.get("identityProviderName") is not None:
        out["identity_provider_name"] = data["identityProviderName"]
    if data.get("identityProviderType") is not None:
        out["identity_provider_type"] = data["identityProviderType"]
    return out


def redact_sensitive(value: IdentityProviderSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "identity_provider_name" in value:
        out["identity_provider_name"] = "*** Sensitive Data Redacted ***"
    return out
