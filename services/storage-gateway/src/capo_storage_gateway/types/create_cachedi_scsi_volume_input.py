"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateCachediSCSIVolumeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.client_token
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.kms_key
    import capo_storage_gateway.types.long
    import capo_storage_gateway.types.network_interface_id
    import capo_storage_gateway.types.snapshot_id
    import capo_storage_gateway.types.tags
    import capo_storage_gateway.types.target_name
    import capo_storage_gateway.types.volume_arn


class CreateCachediSCSIVolumeInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    volume_size_in_bytes: "capo_storage_gateway.types.long.long"
    """<p>The size of the volume in bytes.</p>"""
    snapshot_id: NotRequired["capo_storage_gateway.types.snapshot_id.SnapshotId"]
    """<p>The snapshot ID (e.g. "snap-1122aabb") of the snapshot to restore as the new cached volume. Specify this field if you want to create the iSCSI storage volume from a snapshot; otherwise, do not include this field. To list snapshots for your account use <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html">DescribeSnapshots</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p>"""
    target_name: "capo_storage_gateway.types.target_name.TargetName"
    """<p>The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying <code>TargetName</code> as <i>myvolume</i> results in the target ARN of <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume</code>. The target name must be unique across all volumes on a gateway.</p> <p>If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.</p>"""
    source_volume_arn: NotRequired["capo_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The <code>VolumeSizeInBytes</code> value for this new volume must be equal to or larger than the size of the existing volume, in bytes.</p>"""
    network_interface_id: (
        "capo_storage_gateway.types.network_interface_id.NetworkInterfaceId"
    )
    """<p>The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use <a>DescribeGatewayInformation</a> to get a list of the network interfaces available on a gateway.</p> <p>Valid Values: A valid IP address.</p>"""
    client_token: "capo_storage_gateway.types.client_token.ClientToken"
    """<p>A unique identifier that you use to retry a request. If you retry a request, use the same <code>ClientToken</code> you specified in the initial request.</p>"""
    kms_encrypted: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    kms_key: NotRequired["capo_storage_gateway.types.kms_key.KMSKey"]
    """<p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that you can assign to a cached volume. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers that you can represent in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256 characters.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCachediSCSIVolumeInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["VolumeSizeInBytes"] = value.get("volume_size_in_bytes", 0)
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    out["TargetName"] = value["target_name"]
    if "source_volume_arn" in value:
        out["SourceVolumeARN"] = value["source_volume_arn"]
    out["NetworkInterfaceId"] = value["network_interface_id"]
    out["ClientToken"] = value["client_token"]
    if "kms_encrypted" in value:
        out["KMSEncrypted"] = value["kms_encrypted"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCachediSCSIVolumeInput:
    out: CreateCachediSCSIVolumeInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("CreateCachediSCSIVolumeInput.gateway_arn required")
    if data.get("VolumeSizeInBytes") is not None:
        out["volume_size_in_bytes"] = data["VolumeSizeInBytes"]
    else:
        out["volume_size_in_bytes"] = 0
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("TargetName") is not None:
        out["target_name"] = data["TargetName"]
    else:
        raise DeserializationError("CreateCachediSCSIVolumeInput.target_name required")
    if data.get("SourceVolumeARN") is not None:
        out["source_volume_arn"] = data["SourceVolumeARN"]
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    else:
        raise DeserializationError(
            "CreateCachediSCSIVolumeInput.network_interface_id required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateCachediSCSIVolumeInput.client_token required")
    if data.get("KMSEncrypted") is not None:
        out["kms_encrypted"] = data["KMSEncrypted"]
    if data.get("KMSKey") is not None:
        out["kms_key"] = data["KMSKey"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
