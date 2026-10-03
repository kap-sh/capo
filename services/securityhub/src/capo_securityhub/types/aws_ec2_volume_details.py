"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VolumeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_volume_attachment_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEc2VolumeDetails(TypedDict, closed=True):
    create_time: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the volume was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    device_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The device name for the volume that is attached to the instance. </p>"""
    encrypted: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether the volume is encrypted.</p>"""
    size: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The size of the volume, in GiBs.</p>"""
    snapshot_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The snapshot from which the volume was created.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The volume state. Valid values are as follows:</p> <ul> <li> <p> <code>available</code> </p> </li> <li> <p> <code>creating</code> </p> </li> <li> <p> <code>deleted</code> </p> </li> <li> <p> <code>deleting</code> </p> </li> <li> <p> <code>error</code> </p> </li> <li> <p> <code>in-use</code> </p> </li> </ul>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the KMS key that was used to protect the volume encryption key for the volume.</p>"""
    attachments: NotRequired[
        "capo_securityhub.types.aws_ec2_volume_attachment_list.AwsEc2VolumeAttachmentList"
    ]
    """<p>The volume attachments.</p>"""
    volume_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the volume. </p>"""
    volume_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The volume type. </p>"""
    volume_scan_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether the volume was scanned or skipped. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VolumeDetails) -> dict:
    out: dict = {}
    if "create_time" in value:
        out["CreateTime"] = value["create_time"]
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "size" in value:
        out["Size"] = value["size"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "status" in value:
        out["Status"] = value["status"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "attachments" in value:
        import capo_securityhub.types.aws_ec2_volume_attachment_list

        out["Attachments"] = (
            capo_securityhub.types.aws_ec2_volume_attachment_list.serialize_json(
                value["attachments"]
            )
        )
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "volume_type" in value:
        out["VolumeType"] = value["volume_type"]
    if "volume_scan_status" in value:
        out["VolumeScanStatus"] = value["volume_scan_status"]
    return out


def deserialize_json(data: dict) -> AwsEc2VolumeDetails:
    out: AwsEc2VolumeDetails = {}  # type: ignore[typeddict-item]
    if data.get("CreateTime") is not None:
        out["create_time"] = data["CreateTime"]
    if data.get("DeviceName") is not None:
        out["device_name"] = data["DeviceName"]
    if data.get("Encrypted") is not None:
        out["encrypted"] = data["Encrypted"]
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("Attachments") is not None:
        import capo_securityhub.types.aws_ec2_volume_attachment_list

        out["attachments"] = (
            capo_securityhub.types.aws_ec2_volume_attachment_list.deserialize_json(
                data["Attachments"]
            )
        )
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    if data.get("VolumeType") is not None:
        out["volume_type"] = data["VolumeType"]
    if data.get("VolumeScanStatus") is not None:
        out["volume_scan_status"] = data["VolumeScanStatus"]
    return out
