"""Generated from Smithy shape ``com.amazonaws.cloudfront#InvalidationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class InvalidationSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The unique ID for an invalidation request.</p>"""
    create_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The time that an invalidation request was created.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The status of an invalidation request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InvalidationSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["create_time"], el, "CreateTime"
    )
    SubElement(el, "Status").text = str(value["status"])


def deserialize_xml(el: Element) -> InvalidationSummary:
    out: InvalidationSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import capo_cloudfront.types.timestamp

        out["create_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_create_time
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        out["status"] = ""
    return out
