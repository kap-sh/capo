"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListIdentityProvidersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.identity_provider_list
    import capo_workspaces_web.types.pagination_token


class ListIdentityProvidersResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    identity_providers: NotRequired[
        "capo_workspaces_web.types.identity_provider_list.IdentityProviderList"
    ]
    """<p>The identity providers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityProvidersResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "identity_providers" in value:
        import capo_workspaces_web.types.identity_provider_list

        out["identityProviders"] = (
            capo_workspaces_web.types.identity_provider_list.serialize_json(
                value["identity_providers"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListIdentityProvidersResponse:
    out: ListIdentityProvidersResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("identityProviders") is not None:
        import capo_workspaces_web.types.identity_provider_list

        out["identity_providers"] = (
            capo_workspaces_web.types.identity_provider_list.deserialize_json(
                data["identityProviders"]
            )
        )
    return out


def redact_sensitive(value: ListIdentityProvidersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "identity_providers" in value:
        import capo_workspaces_web.types.identity_provider_list

        out["identity_providers"] = (
            capo_workspaces_web.types.identity_provider_list.redact_sensitive(
                value["identity_providers"]
            )
        )
    return out
