"""Generated from Smithy shape ``com.amazonaws.s3#Transition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.date
    import capo_s3.types.days
    import capo_s3.types.transition_storage_class


class Transition(TypedDict, closed=True):
    date: NotRequired["capo_s3.types.date.Date"]
    """<p>Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.</p>"""
    days: NotRequired["capo_s3.types.days.Days"]
    """<p>Indicates the number of days after creation when objects are transitioned to the specified storage class. The value can be <code>0</code> or any positive integer. Be aware that some storage classes have a minimum storage duration and that you're charged for transitioning objects before their minimum storage duration. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html#lifecycle-configuration-constraints"> Constraints and considerations for transitions</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    storage_class: NotRequired[
        "capo_s3.types.transition_storage_class.TransitionStorageClass"
    ]
    """<p>The storage class to which you want the object to transition.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Transition, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "date" in value:
        import capo_s3.types.date

        capo_s3.types.date.serialize_xml(value["date"], el, "Date")
    if "days" in value:
        SubElement(el, "Days").text = str(value["days"])
    if "storage_class" in value:
        import capo_s3.types.transition_storage_class

        capo_s3.types.transition_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )


def deserialize_xml(el: Element) -> Transition:
    out: Transition = {}  # type: ignore[typeddict-item]
    child_date = el.find("Date")
    if child_date is not None:
        import capo_s3.types.date

        out["date"] = capo_s3.types.date.deserialize_xml(child_date)
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.transition_storage_class

        out["storage_class"] = capo_s3.types.transition_storage_class.deserialize_xml(
            child_storage_class
        )
    return out
