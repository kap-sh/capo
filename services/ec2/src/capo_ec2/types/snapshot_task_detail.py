"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotTaskDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.double
    import capo_ec2.types.sensitive_url
    import capo_ec2.types.string
    import capo_ec2.types.user_bucket_details


class SnapshotTaskDetail(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the disk image being imported.</p>"""
    disk_image_size: NotRequired["capo_ec2.types.double.Double"]
    """<p>The size of the disk in the snapshot, in GiB.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    format: NotRequired["capo_ec2.types.string.String"]
    """<p>The format of the disk image from which the snapshot is created.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The identifier for the KMS key that was used to create the encrypted snapshot.</p>"""
    progress: NotRequired["capo_ec2.types.string.String"]
    """<p>The percentage of completion for the import snapshot task.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The snapshot ID of the disk being imported.</p>"""
    status: NotRequired["capo_ec2.types.string.String"]
    """<p>A brief status for the import snapshot task.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A detailed status message for the import snapshot task.</p>"""
    url: NotRequired["capo_ec2.types.sensitive_url.SensitiveUrl"]
    """<p>The URL of the disk image from which the snapshot is created.</p>"""
    user_bucket: NotRequired["capo_ec2.types.user_bucket_details.UserBucketDetails"]
    """<p>The Amazon S3 bucket for the disk image.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotTaskDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "disk_image_size" in value:
        pairs.append(
            (
                f"{key_prefix}DiskImageSize",
                (
                    "NaN"
                    if value["disk_image_size"] != value["disk_image_size"]
                    else "Infinity"
                    if value["disk_image_size"] == float("inf")
                    else "-Infinity"
                    if value["disk_image_size"] == float("-inf")
                    else str(value["disk_image_size"])
                ),
            )
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "format" in value:
        pairs.append((f"{key_prefix}Format", str(value["format"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "progress" in value:
        pairs.append((f"{key_prefix}Progress", str(value["progress"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "status_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["status_message"])))
    if "url" in value:
        pairs.append((f"{key_prefix}Url", str(value["url"])))
    if "user_bucket" in value:
        import capo_ec2.types.user_bucket_details

        capo_ec2.types.user_bucket_details.serialize_ec2_query(
            value["user_bucket"], pairs, f"{key_prefix}UserBucket"
        )


def deserialize_ec2_query(el: Element) -> SnapshotTaskDetail:
    out: SnapshotTaskDetail = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_disk_image_size = el.find("diskImageSize")
    if child_disk_image_size is not None:
        out["disk_image_size"] = float(child_disk_image_size.text or "")
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_format = el.find("format")
    if child_format is not None:
        out["format"] = str(child_format.text or "")
    child_kms_key_id = el.find("kmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_progress = el.find("progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_status = el.find("status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("statusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_url = el.find("url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    child_user_bucket = el.find("userBucket")
    if child_user_bucket is not None:
        import capo_ec2.types.user_bucket_details

        out["user_bucket"] = capo_ec2.types.user_bucket_details.deserialize_ec2_query(
            child_user_bucket
        )
    return out


def redact_sensitive(value: SnapshotTaskDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
