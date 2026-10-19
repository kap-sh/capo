"""Generated from Smithy shape ``com.amazonaws.cloudfront#Invalidation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.invalidation_batch
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp


class Invalidation(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The identifier for the invalidation request. For example: <code>IDFDVBD632BHDS5</code>.</p>"""
    status: "capo_cloudfront.types.string.string"
    """<p>The status of the invalidation request. When the invalidation batch is finished, the status is <code>Completed</code>.</p>"""
    create_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The date and time the invalidation request was first made.</p>"""
    invalidation_batch: "capo_cloudfront.types.invalidation_batch.InvalidationBatch"
    """<p>The current invalidation information for the batch request.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: Invalidation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Status").text = str(value["status"])
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["create_time"], el, "CreateTime"
    )
    import capo_cloudfront.types.invalidation_batch

    capo_cloudfront.types.invalidation_batch.serialize_xml(
        value["invalidation_batch"], el, "InvalidationBatch"
    )


def deserialize_xml(el: Element) -> Invalidation:
    out: Invalidation = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        out["id"] = ""
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        out["status"] = ""
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
    child_invalidation_batch = el.find("InvalidationBatch")
    if child_invalidation_batch is not None:
        import capo_cloudfront.types.invalidation_batch

        out["invalidation_batch"] = (
            capo_cloudfront.types.invalidation_batch.deserialize_xml(
                child_invalidation_batch
            )
        )
    else:
        raise DeserializationError("Invalidation.invalidation_batch required")
    return out
