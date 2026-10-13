"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotDiskContainer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.sensitive_url
    import capo_ec2.types.string
    import capo_ec2.types.user_bucket


class SnapshotDiskContainer(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the disk image being imported.</p>"""
    format: NotRequired["capo_ec2.types.string.String"]
    """<p>The format of the disk image being imported.</p> <p>Valid values: <code>VHD</code> | <code>VMDK</code> | <code>RAW</code> </p>"""
    url: NotRequired["capo_ec2.types.sensitive_url.SensitiveUrl"]
    """<p>The URL to the Amazon S3-based disk image being imported. It can either be a https URL (https://..) or an Amazon S3 URL (s3://..).</p>"""
    user_bucket: NotRequired["capo_ec2.types.user_bucket.UserBucket"]
    """<p>The Amazon S3 bucket for the disk image.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotDiskContainer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "format" in value:
        pairs.append((f"{key_prefix}Format", str(value["format"])))
    if "url" in value:
        pairs.append((f"{key_prefix}Url", str(value["url"])))
    if "user_bucket" in value:
        import capo_ec2.types.user_bucket

        capo_ec2.types.user_bucket.serialize_ec2_query(
            value["user_bucket"], pairs, f"{key_prefix}UserBucket"
        )


def deserialize_ec2_query(el: Element) -> SnapshotDiskContainer:
    out: SnapshotDiskContainer = {}  # type: ignore[typeddict-item]
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_format = el.find("Format")
    if child_format is not None:
        out["format"] = str(child_format.text or "")
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    child_user_bucket = el.find("UserBucket")
    if child_user_bucket is not None:
        import capo_ec2.types.user_bucket

        out["user_bucket"] = capo_ec2.types.user_bucket.deserialize_ec2_query(
            child_user_bucket
        )
    return out


def redact_sensitive(value: SnapshotDiskContainer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
