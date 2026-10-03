"""Generated from Smithy shape ``com.amazonaws.s3control#NoncurrentVersionExpiration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.days
    import capo_s3_control.types.noncurrent_version_count


class NoncurrentVersionExpiration(TypedDict, closed=True):
    noncurrent_days: "capo_s3_control.types.days.Days"
    """<p>Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations">How Amazon S3 Calculates When an Object Became Noncurrent</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    newer_noncurrent_versions: NotRequired[
        "capo_s3_control.types.noncurrent_version_count.NoncurrentVersionCount"
    ]
    """<p>Specifies how many noncurrent versions S3 on Outposts will retain. If there are this many more recent noncurrent versions, S3 on Outposts will take the associated action. For more information about noncurrent versions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html">Lifecycle configuration elements</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: NoncurrentVersionExpiration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "NoncurrentDays").text = str(value.get("noncurrent_days", 0))
    if "newer_noncurrent_versions" in value:
        SubElement(el, "NewerNoncurrentVersions").text = str(
            value["newer_noncurrent_versions"]
        )


def deserialize_xml(el: Element) -> NoncurrentVersionExpiration:
    out: NoncurrentVersionExpiration = {}  # type: ignore[typeddict-item]
    child_noncurrent_days = el.find("NoncurrentDays")
    if child_noncurrent_days is not None:
        out["noncurrent_days"] = int(child_noncurrent_days.text or "")
    else:
        out["noncurrent_days"] = 0
    child_newer_noncurrent_versions = el.find("NewerNoncurrentVersions")
    if child_newer_noncurrent_versions is not None:
        out["newer_noncurrent_versions"] = int(
            child_newer_noncurrent_versions.text or ""
        )
    return out
