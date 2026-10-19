"""Generated from Smithy shape ``com.amazonaws.cloudfront#KeyValueStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class KeyValueStore(TypedDict, closed=True):
    name: "capo_cloudfront.types.string.string"
    """<p>The name of the key value store.</p>"""
    id: "capo_cloudfront.types.string.string"
    """<p>The unique Id for the key value store.</p>"""
    comment: "capo_cloudfront.types.string.string"
    """<p>A comment for the key value store.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The Amazon Resource Name (ARN) of the key value store.</p>"""
    status: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The status of the key value store.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The last-modified time of the key value store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyValueStore, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Comment").text = str(value["comment"])
    SubElement(el, "ARN").text = str(value["arn"])
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )


def deserialize_xml(el: Element) -> KeyValueStore:
    out: KeyValueStore = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    else:
        out["comment"] = ""
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        out["arn"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
