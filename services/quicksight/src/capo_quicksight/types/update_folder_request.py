"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFolderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.folder_name
    import capo_quicksight.types.restrictive_resource_id


class UpdateFolderRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the folder to update.</p>"""
    folder_id: "capo_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    """<p>The ID of the folder.</p>"""
    name: "capo_quicksight.types.folder_name.FolderName"
    """<p>The name of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFolderRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateFolderRequest:
    out: UpdateFolderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
