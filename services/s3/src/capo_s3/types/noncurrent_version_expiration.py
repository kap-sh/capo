"""Generated from Smithy shape ``com.amazonaws.s3#NoncurrentVersionExpiration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.days
    import capo_s3.types.version_count


class NoncurrentVersionExpiration(TypedDict, closed=True):
    noncurrent_days: NotRequired["capo_s3.types.days.Days"]
    """<p>Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. The value must be a non-zero positive integer. For information about the noncurrent days calculations, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations">How Amazon S3 Calculates When an Object Became Noncurrent</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""
    newer_noncurrent_versions: NotRequired["capo_s3.types.version_count.VersionCount"]
    """<p>Specifies how many noncurrent versions Amazon S3 will retain. You can specify up to 100 noncurrent versions to retain. Amazon S3 will permanently delete any additional noncurrent versions beyond the specified number to retain. For more information about noncurrent versions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html">Lifecycle configuration elements</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(
    value: NoncurrentVersionExpiration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "noncurrent_days" in value:
        SubElement(el, "NoncurrentDays").text = str(value["noncurrent_days"])
    if "newer_noncurrent_versions" in value:
        SubElement(el, "NewerNoncurrentVersions").text = str(
            value["newer_noncurrent_versions"]
        )


def deserialize_xml(el: Element) -> NoncurrentVersionExpiration:
    out: NoncurrentVersionExpiration = {}  # type: ignore[typeddict-item]
    child_noncurrent_days = el.find("NoncurrentDays")
    if child_noncurrent_days is not None:
        out["noncurrent_days"] = int(child_noncurrent_days.text or "")
    child_newer_noncurrent_versions = el.find("NewerNoncurrentVersions")
    if child_newer_noncurrent_versions is not None:
        out["newer_noncurrent_versions"] = int(
            child_newer_noncurrent_versions.text or ""
        )
    return out
