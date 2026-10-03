"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filter_operator
    import capo_quicksight.types.folder_filter_attribute
    import capo_quicksight.types.string


class FolderSearchFilter(TypedDict, closed=True):
    operator: NotRequired["capo_quicksight.types.filter_operator.FilterOperator"]
    """<p>The comparison operator that you want to use as a filter, for example <code>"Operator": "StringEquals"</code>. Valid values are <code>"StringEquals"</code> and <code>"StringLike"</code>.</p> <p>If you set the operator value to <code>"StringEquals"</code>, you need to provide an ownership related filter in the <code>"NAME"</code> field and the arn of the user or group whose folders you want to search in the <code>"Value"</code> field. For example, <code>"Name":"DIRECT_QUICKSIGHT_OWNER", "Operator": "StringEquals", "Value": "arn:aws:quicksight:us-east-1:1:user/default/UserName1"</code>.</p> <p>If you set the value to <code>"StringLike"</code>, you need to provide the name of the folders you are searching for. For example, <code>"Name":"FOLDER_NAME", "Operator": "StringLike", "Value": "Test"</code>. The <code>"StringLike"</code> operator only supports the <code>NAME</code> value <code>FOLDER_NAME</code>.</p>"""
    name: NotRequired[
        "capo_quicksight.types.folder_filter_attribute.FolderFilterAttribute"
    ]
    """<p>The name of a value that you want to use in the filter. For example, <code>"Name": "QUICKSIGHT_OWNER"</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>QUICKSIGHT_VIEWER_OR_OWNER</code>: Provide an ARN of a user or group, and any folders with that ARN listed as one of the folder's owners or viewers are returned. Implicit permissions from folders or groups are considered.</p> </li> <li> <p> <code>QUICKSIGHT_OWNER</code>: Provide an ARN of a user or group, and any folders with that ARN listed as one of the owners of the folders are returned. Implicit permissions from folders or groups are considered.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_SOLE_OWNER</code>: Provide an ARN of a user or group, and any folders with that ARN listed as the only owner of the folder are returned. Implicit permissions from folders or groups are not considered.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_OWNER</code>: Provide an ARN of a user or group, and any folders with that ARN listed as one of the owners of the folders are returned. Implicit permissions from folders or groups are not considered.</p> </li> <li> <p> <code>DIRECT_QUICKSIGHT_VIEWER_OR_OWNER</code>: Provide an ARN of a user or group, and any folders with that ARN listed as one of the owners or viewers of the folders are returned. Implicit permissions from folders or groups are not considered. </p> </li> <li> <p> <code>FOLDER_NAME</code>: Any folders whose names have a substring match to this value will be returned.</p> </li> <li> <p> <code>PARENT_FOLDER_ARN</code>: Provide an ARN of a folder, and any folders that are directly under that parent folder are returned. If you choose to use this option and leave the value blank, all root-level folders in the account are returned. </p> </li> </ul>"""
    value: NotRequired["capo_quicksight.types.string.String"]
    """<p>The value of the named item (in this example, <code>PARENT_FOLDER_ARN</code>), that you want to use as a filter. For example, <code>"Value": "arn:aws:quicksight:us-east-1:1:folder/folderId"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FolderSearchFilter) -> dict:
    out: dict = {}
    if "operator" in value:
        import capo_quicksight.types.filter_operator

        out["Operator"] = capo_quicksight.types.filter_operator.serialize_json(
            value["operator"]
        )
    if "name" in value:
        import capo_quicksight.types.folder_filter_attribute

        out["Name"] = capo_quicksight.types.folder_filter_attribute.serialize_json(
            value["name"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> FolderSearchFilter:
    out: FolderSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Operator") is not None:
        import capo_quicksight.types.filter_operator

        out["operator"] = capo_quicksight.types.filter_operator.deserialize_json(
            data["Operator"]
        )
    if data.get("Name") is not None:
        import capo_quicksight.types.folder_filter_attribute

        out["name"] = capo_quicksight.types.folder_filter_attribute.deserialize_json(
            data["Name"]
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
