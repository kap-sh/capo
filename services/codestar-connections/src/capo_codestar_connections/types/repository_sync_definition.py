"""Generated from Smithy shape ``com.amazonaws.codestarconnections#RepositorySyncDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codestar_connections.types.branch_name
    import capo_codestar_connections.types.directory
    import capo_codestar_connections.types.parent
    import capo_codestar_connections.types.target


class RepositorySyncDefinition(TypedDict, closed=True):
    branch: "capo_codestar_connections.types.branch_name.BranchName"
    """<p>The branch specified for a repository sync definition.</p>"""
    directory: "capo_codestar_connections.types.directory.Directory"
    """<p>The configuration file for a repository sync definition. This value comes from creating or updating the <code>config-file</code> field of a <code>sync-configuration</code>.</p>"""
    parent: "capo_codestar_connections.types.parent.Parent"
    """<p>The parent resource specified for a repository sync definition.</p>"""
    target: "capo_codestar_connections.types.target.Target"
    """<p>The target resource specified for a repository sync definition. In some cases, such as CFN_STACK_SYNC, the parent and target resource are the same.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncDefinition) -> dict:
    out: dict = {}
    out["Branch"] = value["branch"]
    out["Directory"] = value["directory"]
    out["Parent"] = value["parent"]
    out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncDefinition:
    out: RepositorySyncDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Branch") is not None:
        out["branch"] = data["Branch"]
    else:
        out["branch"] = ""
    if data.get("Directory") is not None:
        out["directory"] = data["Directory"]
    else:
        out["directory"] = ""
    if data.get("Parent") is not None:
        out["parent"] = data["Parent"]
    else:
        out["parent"] = ""
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        out["target"] = ""
    return out
