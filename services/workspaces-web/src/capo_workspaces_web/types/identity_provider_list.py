"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IdentityProviderList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_web.types.identity_provider_summary

IdentityProviderList: TypeAlias = list[
    "capo_workspaces_web.types.identity_provider_summary.IdentityProviderSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderList) -> list:
    import capo_workspaces_web.types.identity_provider_summary

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_web.types.identity_provider_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdentityProviderList:
    import capo_workspaces_web.types.identity_provider_summary

    out: IdentityProviderList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_workspaces_web.types.identity_provider_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: IdentityProviderList) -> list[Any]:
    import capo_workspaces_web.types.identity_provider_summary

    return [
        capo_workspaces_web.types.identity_provider_summary.redact_sensitive(item)
        for item in value
    ]
