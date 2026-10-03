"""Generated from Smithy shape ``com.amazonaws.ec2#ExportToS3Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.container_format
    import capo_ec2.types.disk_image_format
    import capo_ec2.types.string


class ExportToS3Task(TypedDict, closed=True):
    container_format: NotRequired["capo_ec2.types.container_format.ContainerFormat"]
    """<p>The container format used to combine disk images with metadata (such as OVF). If absent, only the disk image is exported.</p>"""
    disk_image_format: NotRequired["capo_ec2.types.disk_image_format.DiskImageFormat"]
    """<p>The format for the exported image.</p>"""
    s3_bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon S3 bucket for the destination image. The destination bucket must exist and have an access control list (ACL) attached that specifies the Region-specific canonical account ID for the <code>Grantee</code>. For more information about the ACL to your S3 bucket, see <a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html#vmexport-prerequisites">Prerequisites</a> in the VM Import/Export User Guide.</p>"""
    s3_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The encryption key for your S3 bucket.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportToS3Task, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "container_format" in value:
        import capo_ec2.types.container_format

        capo_ec2.types.container_format.serialize_ec2_query(
            value["container_format"], pairs, f"{key_prefix}ContainerFormat"
        )
    if "disk_image_format" in value:
        import capo_ec2.types.disk_image_format

        capo_ec2.types.disk_image_format.serialize_ec2_query(
            value["disk_image_format"], pairs, f"{key_prefix}DiskImageFormat"
        )
    if "s3_bucket" in value:
        pairs.append((f"{key_prefix}S3Bucket", str(value["s3_bucket"])))
    if "s3_key" in value:
        pairs.append((f"{key_prefix}S3Key", str(value["s3_key"])))


def deserialize_ec2_query(el: Element) -> ExportToS3Task:
    out: ExportToS3Task = {}  # type: ignore[typeddict-item]
    child_container_format = el.find("containerFormat")
    if child_container_format is not None:
        import capo_ec2.types.container_format

        out["container_format"] = capo_ec2.types.container_format.deserialize_ec2_query(
            child_container_format
        )
    child_disk_image_format = el.find("diskImageFormat")
    if child_disk_image_format is not None:
        import capo_ec2.types.disk_image_format

        out["disk_image_format"] = (
            capo_ec2.types.disk_image_format.deserialize_ec2_query(
                child_disk_image_format
            )
        )
    child_s3_bucket = el.find("s3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_key = el.find("s3Key")
    if child_s3_key is not None:
        out["s3_key"] = str(child_s3_key.text or "")
    return out
