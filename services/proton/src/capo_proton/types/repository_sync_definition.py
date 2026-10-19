"""Generated from Smithy shape ``com.amazonaws.proton#RepositorySyncDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.git_branch_name


class RepositorySyncDefinition(TypedDict, closed=True):
    target: "str"
    """<p>The resource that is synced to.</p>"""
    parent: "str"
    """<p>The resource that is synced from.</p>"""
    branch: "capo_proton.types.git_branch_name.GitBranchName"
    """<p>The repository branch.</p>"""
    directory: "str"
    """<p>The directory in the repository.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncDefinition) -> dict:
    out: dict = {}
    out["target"] = value["target"]
    out["parent"] = value["parent"]
    out["branch"] = value["branch"]
    out["directory"] = value["directory"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncDefinition:
    out: RepositorySyncDefinition = {}  # type: ignore[typeddict-item]
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
    if data.get("parent") is not None:
        out["parent"] = data["parent"]
    else:
        out["parent"] = ""
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    else:
        out["branch"] = ""
    if data.get("directory") is not None:
        out["directory"] = data["directory"]
    else:
        out["directory"] = ""
    return out
