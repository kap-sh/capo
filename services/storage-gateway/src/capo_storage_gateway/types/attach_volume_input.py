"""Generated from Smithy shape ``com.amazonaws.storagegateway#AttachVolumeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.disk_id
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.network_interface_id
    import capo_storage_gateway.types.target_name
    import capo_storage_gateway.types.volume_arn


class AttachVolumeInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The Amazon Resource Name (ARN) of the gateway that you want to attach the volume to.</p>"""
    target_name: NotRequired["capo_storage_gateway.types.target_name.TargetName"]
    """<p>The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying <code>TargetName</code> as <i>myvolume</i> results in the target ARN of <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume</code>. The target name must be unique across all volumes on a gateway.</p> <p>If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.</p>"""
    volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN"
    """<p>The Amazon Resource Name (ARN) of the volume to attach to the specified gateway.</p>"""
    network_interface_id: (
        "capo_storage_gateway.types.network_interface_id.NetworkInterfaceId"
    )
    """<p>The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use <a>DescribeGatewayInformation</a> to get a list of the network interfaces available on a gateway.</p> <p>Valid Values: A valid IP address.</p>"""
    disk_id: NotRequired["capo_storage_gateway.types.disk_id.DiskId"]
    """<p>The unique device ID or other distinguishing data that identifies the local disk used to create the volume. This value is only required when you are attaching a stored volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachVolumeInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "target_name" in value:
        out["TargetName"] = value["target_name"]
    out["VolumeARN"] = value["volume_arn"]
    out["NetworkInterfaceId"] = value["network_interface_id"]
    if "disk_id" in value:
        out["DiskId"] = value["disk_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachVolumeInput:
    out: AttachVolumeInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("TargetName") is not None:
        out["target_name"] = data["TargetName"]
    if data.get("VolumeARN") is not None:
        out["volume_arn"] = data["VolumeARN"]
    else:
        out["volume_arn"] = ""
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    else:
        out["network_interface_id"] = ""
    if data.get("DiskId") is not None:
        out["disk_id"] = data["DiskId"]
    return out
