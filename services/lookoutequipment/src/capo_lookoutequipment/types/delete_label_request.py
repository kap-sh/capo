"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DeleteLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.label_id


class DeleteLabelRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> The name of the label group that contains the label that you want to delete. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    label_id: "capo_lookoutequipment.types.label_id.LabelId"
    """<p> The ID of the label that you want to delete. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteLabelRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    out["LabelId"] = value["label_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteLabelRequest:
    out: DeleteLabelRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelGroupName") is not None:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        out["label_group_name"] = ""
    if data.get("LabelId") is not None:
        out["label_id"] = data["LabelId"]
    else:
        out["label_id"] = ""
    return out
