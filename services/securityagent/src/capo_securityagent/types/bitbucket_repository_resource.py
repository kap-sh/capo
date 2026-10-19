"""Generated from Smithy shape ``com.amazonaws.securityagent#BitbucketRepositoryResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.bitbucket_workspace
    import capo_securityagent.types.provider_resource_name


class BitbucketRepositoryResource(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    workspace: "capo_securityagent.types.bitbucket_workspace.BitbucketWorkspace"
    """<p>The workspace slug that owns the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BitbucketRepositoryResource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["workspace"] = value["workspace"]
    return out


def deserialize_json(data: dict) -> BitbucketRepositoryResource:
    out: BitbucketRepositoryResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("workspace") is not None:
        out["workspace"] = data["workspace"]
    else:
        out["workspace"] = ""
    return out
