"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BranchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.branch_name


class BranchFilter(TypedDict, closed=True):
    name: "capo_bedrock_agentcore.types.branch_name.BranchName"
    """<p>The name of the branch to filter by.</p>"""
    include_parent_branches: "bool"
    """<p>Specifies whether to include parent branches in the results. Set to true to include parent branches, or false to exclude them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BranchFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["includeParentBranches"] = value.get("include_parent_branches", True)
    return out


def deserialize_json(data: dict) -> BranchFilter:
    out: BranchFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("includeParentBranches") is not None:
        out["include_parent_branches"] = data["includeParentBranches"]
    else:
        out["include_parent_branches"] = True
    return out
