"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.group_description
    import capo_quicksight.types.group_name
    import capo_quicksight.types.namespace


class CreateGroupRequest(TypedDict, closed=True):
    group_name: "capo_quicksight.types.group_name.GroupName"
    """<p>A name for the group that you want to create.</p>"""
    description: NotRequired["capo_quicksight.types.group_description.GroupDescription"]
    """<p>A description for the group that you want to create.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that you want the group to be a part of.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGroupRequest) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateGroupRequest:
    out: CreateGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
