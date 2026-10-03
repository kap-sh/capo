"""Generated from Smithy shape ``com.amazonaws.s3control#LifecycleExpiration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.date
    import capo_s3_control.types.days
    import capo_s3_control.types.expired_object_delete_marker


class LifecycleExpiration(TypedDict, closed=True):
    date: NotRequired["capo_s3_control.types.date.Date"]
    """<p>Indicates at what date the object is to be deleted. Should be in GMT ISO 8601 format.</p>"""
    days: "capo_s3_control.types.days.Days"
    """<p>Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a non-zero positive integer.</p>"""
    expired_object_delete_marker: (
        "capo_s3_control.types.expired_object_delete_marker.ExpiredObjectDeleteMarker"
    )
    """<p>Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the delete marker will be expired. If set to false, the policy takes no action. This cannot be specified with Days or Date in a Lifecycle Expiration Policy. To learn more about delete markers, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html">Working with delete markers</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LifecycleExpiration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "date" in value:
        import capo_s3_control.types.date

        capo_s3_control.types.date.serialize_xml(value["date"], el, "Date")
    SubElement(el, "Days").text = str(value.get("days", 0))
    SubElement(el, "ExpiredObjectDeleteMarker").text = (
        "true" if value.get("expired_object_delete_marker", False) else "false"
    )


def deserialize_xml(el: Element) -> LifecycleExpiration:
    out: LifecycleExpiration = {}  # type: ignore[typeddict-item]
    child_date = el.find("Date")
    if child_date is not None:
        import capo_s3_control.types.date

        out["date"] = capo_s3_control.types.date.deserialize_xml(child_date)
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    else:
        out["days"] = 0
    child_expired_object_delete_marker = el.find("ExpiredObjectDeleteMarker")
    if child_expired_object_delete_marker is not None:
        out["expired_object_delete_marker"] = (
            child_expired_object_delete_marker.text or ""
        ).lower() == "true"
    else:
        out["expired_object_delete_marker"] = False
    return out
