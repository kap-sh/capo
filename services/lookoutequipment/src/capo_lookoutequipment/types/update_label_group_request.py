"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateLabelGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.fault_codes
    import capo_lookoutequipment.types.label_group_name


class UpdateLabelGroupRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> The name of the label group to be updated. </p>"""
    fault_codes: NotRequired["capo_lookoutequipment.types.fault_codes.FaultCodes"]
    """<p> Updates the code indicating the type of anomaly associated with the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateLabelGroupRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    if "fault_codes" in value:
        import capo_lookoutequipment.types.fault_codes

        out["FaultCodes"] = (
            capo_lookoutequipment.types.fault_codes.serialize_aws_json_1_0(
                value["fault_codes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateLabelGroupRequest:
    out: UpdateLabelGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("LabelGroupName") is not None:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        out["label_group_name"] = ""
    if data.get("FaultCodes") is not None:
        import capo_lookoutequipment.types.fault_codes

        out["fault_codes"] = (
            capo_lookoutequipment.types.fault_codes.deserialize_aws_json_1_0(
                data["FaultCodes"]
            )
        )
    return out
