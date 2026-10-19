"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateLabelGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.fault_codes
    import capo_lookoutequipment.types.idempotence_token
    import capo_lookoutequipment.types.label_group_name
    import capo_lookoutequipment.types.tag_list


class CreateLabelGroupRequest(TypedDict, closed=True):
    label_group_name: "capo_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> Names a group of labels.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data. </p>"""
    fault_codes: NotRequired["capo_lookoutequipment.types.fault_codes.FaultCodes"]
    """<p> The acceptable fault codes (indicating the type of anomaly associated with the label) that can be used with this label group.</p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""
    client_token: "capo_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p> A unique identifier for the request to create a label group. If you do not set the client request token, Lookout for Equipment generates one. </p>"""
    tags: NotRequired["capo_lookoutequipment.types.tag_list.TagList"]
    """<p> Tags that provide metadata about the label group you are creating. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateLabelGroupRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    if "fault_codes" in value:
        import capo_lookoutequipment.types.fault_codes

        out["FaultCodes"] = (
            capo_lookoutequipment.types.fault_codes.serialize_aws_json_1_0(
                value["fault_codes"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_lookoutequipment.types.tag_list

        out["Tags"] = capo_lookoutequipment.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateLabelGroupRequest:
    out: CreateLabelGroupRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("Tags") is not None:
        import capo_lookoutequipment.types.tag_list

        out["tags"] = capo_lookoutequipment.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
