"""Generated from Smithy shape ``com.amazonaws.s3#NoncurrentVersionTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.days
    import capo_s3.types.transition_storage_class
    import capo_s3.types.version_count


class NoncurrentVersionTransition(TypedDict, closed=True):
    noncurrent_days: NotRequired["capo_s3.types.days.Days"]
    """<p>Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations">How Amazon S3 Calculates How Long an Object Has Been Noncurrent</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    storage_class: NotRequired[
        "capo_s3.types.transition_storage_class.TransitionStorageClass"
    ]
    """<p>The class of storage used to store the object.</p>"""
    newer_noncurrent_versions: NotRequired["capo_s3.types.version_count.VersionCount"]
    """<p>Specifies how many noncurrent versions Amazon S3 will retain in the same storage class before transitioning objects. You can specify up to 100 noncurrent versions to retain. Amazon S3 will transition any additional noncurrent versions beyond the specified number to retain. For more information about noncurrent versions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html">Lifecycle configuration elements</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: NoncurrentVersionTransition, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "noncurrent_days" in value:
        SubElement(el, "NoncurrentDays").text = str(value["noncurrent_days"])
    if "storage_class" in value:
        import capo_s3.types.transition_storage_class

        capo_s3.types.transition_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "newer_noncurrent_versions" in value:
        SubElement(el, "NewerNoncurrentVersions").text = str(
            value["newer_noncurrent_versions"]
        )


def deserialize_xml(el: Element) -> NoncurrentVersionTransition:
    out: NoncurrentVersionTransition = {}  # type: ignore[typeddict-item]
    child_noncurrent_days = el.find("NoncurrentDays")
    if child_noncurrent_days is not None:
        out["noncurrent_days"] = int(child_noncurrent_days.text or "")
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.transition_storage_class

        out["storage_class"] = capo_s3.types.transition_storage_class.deserialize_xml(
            child_storage_class
        )
    child_newer_noncurrent_versions = el.find("NewerNoncurrentVersions")
    if child_newer_noncurrent_versions is not None:
        out["newer_noncurrent_versions"] = int(
            child_newer_noncurrent_versions.text or ""
        )
    return out
