"""Generated from Smithy shape ``com.amazonaws.s3control#NoncurrentVersionTransition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.days
    import capo_s3_control.types.transition_storage_class


class NoncurrentVersionTransition(TypedDict, closed=True):
    noncurrent_days: "capo_s3_control.types.days.Days"
    """<p>Specifies the number of days an object is noncurrent before Amazon S3 can perform the associated action. For information about the noncurrent days calculations, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html#non-current-days-calculations"> How Amazon S3 Calculates How Long an Object Has Been Noncurrent</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    storage_class: NotRequired[
        "capo_s3_control.types.transition_storage_class.TransitionStorageClass"
    ]
    """<p>The class of storage used to store the object.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: NoncurrentVersionTransition, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "NoncurrentDays").text = str(value.get("noncurrent_days", 0))
    if "storage_class" in value:
        import capo_s3_control.types.transition_storage_class

        capo_s3_control.types.transition_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )


def deserialize_xml(el: Element) -> NoncurrentVersionTransition:
    out: NoncurrentVersionTransition = {}  # type: ignore[typeddict-item]
    child_noncurrent_days = el.find("NoncurrentDays")
    if child_noncurrent_days is not None:
        out["noncurrent_days"] = int(child_noncurrent_days.text or "")
    else:
        out["noncurrent_days"] = 0
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3_control.types.transition_storage_class

        out["storage_class"] = (
            capo_s3_control.types.transition_storage_class.deserialize_xml(
                child_storage_class
            )
        )
    return out
