"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DeleteLabelGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.label_group_name


class DeleteLabelGroupRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> The name of the label group that you want to delete. Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteLabelGroupRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteLabelGroupRequest:
    out: DeleteLabelGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelGroupName") is not None:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        out["label_group_name"] = ""
    return out
