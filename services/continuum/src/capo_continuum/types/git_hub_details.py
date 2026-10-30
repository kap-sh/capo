"""Generated from Smithy shape ``com.amazonaws.continuum#GitHubDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.git_hub_organization_name


class GitHubDetails(TypedDict, closed=True):
    organization_name: NotRequired[
        "capo_continuum.types.git_hub_organization_name.GitHubOrganizationName"
    ]
    """The name of the GitHub organization associated with the integration."""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubDetails) -> dict:
    out: dict = {}
    if "organization_name" in value:
        out["organizationName"] = value["organization_name"]
    return out


def deserialize_json(data: dict) -> GitHubDetails:
    out: GitHubDetails = {}  # type: ignore[typeddict-item]
    if data.get("organizationName") is not None:
        out["organization_name"] = data["organizationName"]
    return out
