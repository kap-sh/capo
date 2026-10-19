"""Generated from Smithy shape ``com.amazonaws.securityagent#GitHubRepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.access_type
    import capo_securityagent.types.git_hub_owner
    import capo_securityagent.types.provider_resource_id
    import capo_securityagent.types.provider_resource_name


class GitHubRepositoryMetadata(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    """<p>The name of the GitHub repository.</p>"""
    provider_resource_id: (
        "capo_securityagent.types.provider_resource_id.ProviderResourceId"
    )
    """<p>The provider-specific resource identifier for the GitHub repository.</p>"""
    owner: "capo_securityagent.types.git_hub_owner.GitHubOwner"
    """<p>The owner of the GitHub repository.</p>"""
    access_type: NotRequired["capo_securityagent.types.access_type.AccessType"]
    """<p>The access type of the GitHub repository. Valid values are PRIVATE and PUBLIC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubRepositoryMetadata) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["providerResourceId"] = value["provider_resource_id"]
    out["owner"] = value["owner"]
    if "access_type" in value:
        import capo_securityagent.types.access_type

        out["accessType"] = capo_securityagent.types.access_type.serialize_json(
            value["access_type"]
        )
    return out


def deserialize_json(data: dict) -> GitHubRepositoryMetadata:
    out: GitHubRepositoryMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("providerResourceId") is not None:
        out["provider_resource_id"] = data["providerResourceId"]
    else:
        out["provider_resource_id"] = ""
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        out["owner"] = ""
    if data.get("accessType") is not None:
        import capo_securityagent.types.access_type

        out["access_type"] = capo_securityagent.types.access_type.deserialize_json(
            data["accessType"]
        )
    return out
