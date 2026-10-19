"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeLabelGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.label_group_name


class DescribeLabelGroupRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> Returns the name of the label group. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLabelGroupRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeLabelGroupRequest:
    out: DescribeLabelGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelGroupName") is not None:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        out["label_group_name"] = ""
    return out
