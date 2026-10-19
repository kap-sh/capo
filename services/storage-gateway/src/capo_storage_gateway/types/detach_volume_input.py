"""Generated from Smithy shape ``com.amazonaws.storagegateway#DetachVolumeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.volume_arn


class DetachVolumeInput(TypedDict, closed=True):
    volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN"
    """<p>The Amazon Resource Name (ARN) of the volume to detach from the gateway.</p>"""
    force_detach: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to forcibly remove the iSCSI connection of the target volume and detach the volume. The default is <code>false</code>. If this value is set to <code>false</code>, you must manually disconnect the iSCSI connection from the target volume.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachVolumeInput) -> dict:
    out: dict = {}
    out["VolumeARN"] = value["volume_arn"]
    if "force_detach" in value:
        out["ForceDetach"] = value["force_detach"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachVolumeInput:
    out: DetachVolumeInput = {}  # type: ignore[typeddict-item]
    if data.get("VolumeARN") is not None:
        out["volume_arn"] = data["VolumeARN"]
    else:
        out["volume_arn"] = ""
    if data.get("ForceDetach") is not None:
        out["force_detach"] = data["ForceDetach"]
    return out
