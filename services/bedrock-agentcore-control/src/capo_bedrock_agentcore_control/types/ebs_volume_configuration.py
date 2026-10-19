"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EbsVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ebs_snapshot_id
    import capo_bedrock_agentcore_control.types.ebs_volume_type
    import capo_bedrock_agentcore_control.types.kms_key_id
    import capo_bedrock_agentcore_control.types.volume_iops
    import capo_bedrock_agentcore_control.types.volume_name
    import capo_bedrock_agentcore_control.types.volume_size_gi_b
    import capo_bedrock_agentcore_control.types.volume_throughput


class EbsVolumeConfiguration(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.volume_name.VolumeName"
    """<p>The logical name of the volume. Use this name to reference the volume when you mount it into an agent runtime.</p>"""
    size_gi_b: "capo_bedrock_agentcore_control.types.volume_size_gi_b.VolumeSizeGiB"
    """<p>The size of the volume, in GiB.</p>"""
    volume_type: "capo_bedrock_agentcore_control.types.ebs_volume_type.EbsVolumeType"
    """<p>The Amazon EBS volume type. If you do not specify a type, the default is <code>gp3</code>.</p>"""
    iops: NotRequired["capo_bedrock_agentcore_control.types.volume_iops.VolumeIops"]
    """<p>The number of IOPS to provision. Valid only for <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes.</p>"""
    throughput: NotRequired[
        "capo_bedrock_agentcore_control.types.volume_throughput.VolumeThroughput"
    ]
    """<p>The throughput, in MiB/s. Valid only for <code>gp3</code> volumes.</p>"""
    encrypted: NotRequired["bool"]
    """<p>Specifies whether to encrypt the volume. If <code>true</code>, the service encrypts the volume with the KMS key that you specify in <code>kmsKeyId</code>, or the default KMS key for Amazon EBS if you do not specify one. The default is <code>true</code>.</p>"""
    kms_key_id: NotRequired["capo_bedrock_agentcore_control.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for encryption.</p>"""
    snapshot_id: NotRequired[
        "capo_bedrock_agentcore_control.types.ebs_snapshot_id.EbsSnapshotId"
    ]
    """<p>An optional Amazon EBS snapshot ID. If provided, the volume is initialized from this snapshot the first time it is created. On subsequent restarts, the existing volume is used and the snapshot is ignored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumeConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["sizeGiB"] = value["size_gi_b"]
    import capo_bedrock_agentcore_control.types.ebs_volume_type

    out["volumeType"] = (
        capo_bedrock_agentcore_control.types.ebs_volume_type.serialize_json(
            value.get("volume_type", "gp3")
        )
    )
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "snapshot_id" in value:
        out["snapshotId"] = value["snapshot_id"]
    return out


def deserialize_json(data: dict) -> EbsVolumeConfiguration:
    out: EbsVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("sizeGiB") is not None:
        out["size_gi_b"] = data["sizeGiB"]
    else:
        out["size_gi_b"] = 0
    if data.get("volumeType") is not None:
        import capo_bedrock_agentcore_control.types.ebs_volume_type

        out["volume_type"] = (
            capo_bedrock_agentcore_control.types.ebs_volume_type.deserialize_json(
                data["volumeType"]
            )
        )
    else:
        out["volume_type"] = "gp3"
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    if data.get("encrypted") is not None:
        out["encrypted"] = data["encrypted"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("snapshotId") is not None:
        out["snapshot_id"] = data["snapshotId"]
    return out
