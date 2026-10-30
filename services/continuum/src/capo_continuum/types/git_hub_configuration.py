"""Generated from Smithy shape ``com.amazonaws.continuum#GitHubConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_continuum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_continuum.types.git_hub_authorization_configuration
    import capo_continuum.types.git_hub_organization_name


class GitHubConfiguration(TypedDict, closed=True):
    authorization: "capo_continuum.types.git_hub_authorization_configuration.GitHubAuthorizationConfiguration"
    """OAuth authorization used to establish the integration. Required on create; not returned on read operations."""
    organization_name: NotRequired[
        "capo_continuum.types.git_hub_organization_name.GitHubOrganizationName"
    ]
    """The name of the GitHub organization to associate with the integration. If not specified, the integration is associated with the authenticated user's personal account."""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubConfiguration) -> dict:
    out: dict = {}
    import capo_continuum.types.git_hub_authorization_configuration

    out["authorization"] = (
        capo_continuum.types.git_hub_authorization_configuration.serialize_json(
            value["authorization"]
        )
    )
    if "organization_name" in value:
        out["organizationName"] = value["organization_name"]
    return out


def deserialize_json(data: dict) -> GitHubConfiguration:
    out: GitHubConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("authorization") is not None:
        import capo_continuum.types.git_hub_authorization_configuration

        out["authorization"] = (
            capo_continuum.types.git_hub_authorization_configuration.deserialize_json(
                data["authorization"]
            )
        )
    else:
        raise DeserializationError("GitHubConfiguration.authorization required")
    if data.get("organizationName") is not None:
        out["organization_name"] = data["organizationName"]
    return out


def redact_sensitive(value: GitHubConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization" in value:
        import capo_continuum.types.git_hub_authorization_configuration

        out["authorization"] = (
            capo_continuum.types.git_hub_authorization_configuration.redact_sensitive(
                value["authorization"]
            )
        )
    return out
