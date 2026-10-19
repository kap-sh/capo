"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ModifyHapgRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm.types.hapg_arn
    import capo_cloudhsm.types.label
    import capo_cloudhsm.types.partition_serial_list


class ModifyHapgRequest(TypedDict, closed=True):
    hapg_arn: "capo_cloudhsm.types.hapg_arn.HapgArn"
    """<p>The ARN of the high-availability partition group to modify.</p>"""
    label: NotRequired["capo_cloudhsm.types.label.Label"]
    """<p>The new label for the high-availability partition group.</p>"""
    partition_serial_list: NotRequired[
        "capo_cloudhsm.types.partition_serial_list.PartitionSerialList"
    ]
    """<p>The list of partition serial numbers to make members of the high-availability partition group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyHapgRequest) -> dict:
    out: dict = {}
    out["HapgArn"] = value["hapg_arn"]
    if "label" in value:
        out["Label"] = value["label"]
    if "partition_serial_list" in value:
        import capo_cloudhsm.types.partition_serial_list

        out["PartitionSerialList"] = (
            capo_cloudhsm.types.partition_serial_list.serialize_aws_json_1_1(
                value["partition_serial_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyHapgRequest:
    out: ModifyHapgRequest = {}  # type: ignore[typeddict-item]
    if data.get("HapgArn") is not None:
        out["hapg_arn"] = data["HapgArn"]
    else:
        out["hapg_arn"] = ""
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("PartitionSerialList") is not None:
        import capo_cloudhsm.types.partition_serial_list

        out["partition_serial_list"] = (
            capo_cloudhsm.types.partition_serial_list.deserialize_aws_json_1_1(
                data["PartitionSerialList"]
            )
        )
    return out
