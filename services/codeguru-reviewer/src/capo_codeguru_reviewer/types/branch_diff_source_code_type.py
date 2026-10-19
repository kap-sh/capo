"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#BranchDiffSourceCodeType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.branch_name


class BranchDiffSourceCodeType(TypedDict, closed=True):
    source_branch_name: "capo_codeguru_reviewer.types.branch_name.BranchName"
    """<p>The source branch for a diff in an associated repository.</p>"""
    destination_branch_name: "capo_codeguru_reviewer.types.branch_name.BranchName"
    """<p>The destination branch for a diff in an associated repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BranchDiffSourceCodeType) -> dict:
    out: dict = {}
    out["SourceBranchName"] = value["source_branch_name"]
    out["DestinationBranchName"] = value["destination_branch_name"]
    return out


def deserialize_json(data: dict) -> BranchDiffSourceCodeType:
    out: BranchDiffSourceCodeType = {}  # type: ignore[typeddict-item]
    if data.get("SourceBranchName") is not None:
        out["source_branch_name"] = data["SourceBranchName"]
    else:
        out["source_branch_name"] = ""
    if data.get("DestinationBranchName") is not None:
        out["destination_branch_name"] = data["DestinationBranchName"]
    else:
        out["destination_branch_name"] = ""
    return out
