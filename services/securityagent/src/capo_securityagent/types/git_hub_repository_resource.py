"""Generated from Smithy shape ``com.amazonaws.securityagent#GitHubRepositoryResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.git_hub_owner
    import capo_securityagent.types.provider_resource_name


class GitHubRepositoryResource(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    """<p>The name of the GitHub repository.</p>"""
    owner: "capo_securityagent.types.git_hub_owner.GitHubOwner"
    """<p>The owner of the GitHub repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubRepositoryResource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["owner"] = value["owner"]
    return out


def deserialize_json(data: dict) -> GitHubRepositoryResource:
    out: GitHubRepositoryResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    else:
        out["owner"] = ""
    return out
