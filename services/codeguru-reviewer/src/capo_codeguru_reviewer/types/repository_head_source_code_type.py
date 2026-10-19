"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RepositoryHeadSourceCodeType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.branch_name


class RepositoryHeadSourceCodeType(TypedDict, closed=True):
    branch_name: "capo_codeguru_reviewer.types.branch_name.BranchName"
    """<p>The name of the branch in an associated repository. The <code>RepositoryHeadSourceCodeType</code> specifies the tip of this branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryHeadSourceCodeType) -> dict:
    out: dict = {}
    out["BranchName"] = value["branch_name"]
    return out


def deserialize_json(data: dict) -> RepositoryHeadSourceCodeType:
    out: RepositoryHeadSourceCodeType = {}  # type: ignore[typeddict-item]
    if data.get("BranchName") is not None:
        out["branch_name"] = data["BranchName"]
    else:
        out["branch_name"] = ""
    return out
