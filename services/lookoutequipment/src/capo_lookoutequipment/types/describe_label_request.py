"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeLabelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.label_id


class DescribeLabelRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> Returns the name of the group containing the label. </p>"""
    label_id: "capo_lookoutequipment.types.label_id.LabelId"
    """<p> Returns the ID of the label. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLabelRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    out["LabelId"] = value["label_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLabelRequest:
    out: DescribeLabelRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelGroupName") is not None:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        out["label_group_name"] = ""
    if data.get("LabelId") is not None:
        out["label_id"] = data["LabelId"]
    else:
        out["label_id"] = ""
    return out
