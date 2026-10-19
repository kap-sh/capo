"""Generated from Smithy shape ``com.amazonaws.securityagent#GitLabRepositoryResource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.git_lab_namespace
    import capo_securityagent.types.provider_resource_name


class GitLabRepositoryResource(TypedDict, closed=True):
    name: "capo_securityagent.types.provider_resource_name.ProviderResourceName"
    namespace: "capo_securityagent.types.git_lab_namespace.GitLabNamespace"
    """<p>The namespace (group or user path) that owns the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabRepositoryResource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> GitLabRepositoryResource:
    out: GitLabRepositoryResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    return out
