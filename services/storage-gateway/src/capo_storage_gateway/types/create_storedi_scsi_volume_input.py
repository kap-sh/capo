"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateStorediSCSIVolumeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.disk_id
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.kms_key
    import capo_storage_gateway.types.network_interface_id
    import capo_storage_gateway.types.snapshot_id
    import capo_storage_gateway.types.tags
    import capo_storage_gateway.types.target_name


class CreateStorediSCSIVolumeInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    disk_id: "capo_storage_gateway.types.disk_id.DiskId"
    """<p>The unique identifier for the gateway local disk that is configured as a stored volume. Use <a href="https://docs.aws.amazon.com/storagegateway/latest/userguide/API_ListLocalDisks.html">ListLocalDisks</a> to list disk IDs for a gateway.</p>"""
    snapshot_id: NotRequired["capo_storage_gateway.types.snapshot_id.SnapshotId"]
    """<p>The snapshot ID (e.g., "snap-1122aabb") of the snapshot to restore as the new stored volume. Specify this field if you want to create the iSCSI storage volume from a snapshot; otherwise, do not include this field. To list snapshots for your account use <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html">DescribeSnapshots</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p>"""
    preserve_existing_data: "capo_storage_gateway.types.boolean2.Boolean2"
    """<p>Set to <code>true</code> if you want to preserve the data on the local disk. Otherwise, set to <code>false</code> to create an empty volume.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    target_name: "capo_storage_gateway.types.target_name.TargetName"
    """<p>The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying <code>TargetName</code> as <i>myvolume</i> results in the target ARN of <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume</code>. The target name must be unique across all volumes on a gateway.</p> <p>If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.</p>"""
    network_interface_id: (
        "capo_storage_gateway.types.network_interface_id.NetworkInterfaceId"
    )
    """<p>The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use <a>DescribeGatewayInformation</a> to get a list of the network interfaces available on a gateway.</p> <p>Valid Values: A valid IP address.</p>"""
    kms_encrypted: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to use Amazon S3 server-side encryption with your own KMS key, or <code>false</code> to use a key managed by Amazon S3. Optional.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""
    kms_key: NotRequired["capo_storage_gateway.types.kms_key.KMSKey"]
    """<p>The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when <code>KMSEncrypted</code> is <code>true</code>. Optional.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that can be assigned to a stored volume. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStorediSCSIVolumeInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["DiskId"] = value["disk_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    out["PreserveExistingData"] = value.get("preserve_existing_data", False)
    out["TargetName"] = value["target_name"]
    out["NetworkInterfaceId"] = value["network_interface_id"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateStorediSCSIVolumeInput:
    out: CreateStorediSCSIVolumeInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("CreateStorediSCSIVolumeInput.gateway_arn required")
    if data.get("DiskId") is not None:
        out["disk_id"] = data["DiskId"]
    else:
        raise DeserializationError("CreateStorediSCSIVolumeInput.disk_id required")
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("PreserveExistingData") is not None:
        out["preserve_existing_data"] = data["PreserveExistingData"]
    else:
        out["preserve_existing_data"] = False
    if data.get("TargetName") is not None:
        out["target_name"] = data["TargetName"]
    else:
        raise DeserializationError("CreateStorediSCSIVolumeInput.target_name required")
    if data.get("NetworkInterfaceId") is not None:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    else:
        raise DeserializationError(
            "CreateStorediSCSIVolumeInput.network_interface_id required"
        )
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
