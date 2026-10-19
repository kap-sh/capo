"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeChapCredentialsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.target_arn


class DescribeChapCredentialsInput(TypedDict, closed=True):
    target_arn: "capo_storage_gateway.types.target_arn.TargetARN"
    """<p>The Amazon Resource Name (ARN) of the iSCSI volume target. Use the <a>DescribeStorediSCSIVolumes</a> operation to return to retrieve the TargetARN for specified VolumeARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeChapCredentialsInput) -> dict:
    out: dict = {}
    out["TargetARN"] = value["target_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeChapCredentialsInput:
    out: DescribeChapCredentialsInput = {}  # type: ignore[typeddict-item]
    if data.get("TargetARN") is not None:
        out["target_arn"] = data["TargetARN"]
    else:
        out["target_arn"] = ""
    return out
