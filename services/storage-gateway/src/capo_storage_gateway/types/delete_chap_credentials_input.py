"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteChapCredentialsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.iqn_name
    import capo_storage_gateway.types.target_arn


class DeleteChapCredentialsInput(TypedDict, closed=True):
    target_arn: "capo_storage_gateway.types.target_arn.TargetARN"
    """<p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>"""
    initiator_name: "capo_storage_gateway.types.iqn_name.IqnName"
    """<p>The iSCSI initiator that connects to the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteChapCredentialsInput) -> dict:
    out: dict = {}
    out["TargetARN"] = value["target_arn"]
    out["InitiatorName"] = value["initiator_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteChapCredentialsInput:
    out: DeleteChapCredentialsInput = {}  # type: ignore[typeddict-item]
    if data.get("TargetARN") is not None:
        out["target_arn"] = data["TargetARN"]
    else:
        out["target_arn"] = ""
    if data.get("InitiatorName") is not None:
        out["initiator_name"] = data["InitiatorName"]
    else:
        out["initiator_name"] = ""
    return out
