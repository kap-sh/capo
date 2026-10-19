"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateRepositoryNameInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.repository_name


class UpdateRepositoryNameInput(TypedDict, closed=True):
    old_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The current name of the repository.</p>"""
    new_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The new name for the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRepositoryNameInput) -> dict:
    out: dict = {}
    out["oldName"] = value["old_name"]
    out["newName"] = value["new_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRepositoryNameInput:
    out: UpdateRepositoryNameInput = {}  # type: ignore[typeddict-item]
    if data.get("oldName") is not None:
        out["old_name"] = data["oldName"]
    else:
        out["old_name"] = ""
    if data.get("newName") is not None:
        out["new_name"] = data["newName"]
    else:
        out["new_name"] = ""
    return out
