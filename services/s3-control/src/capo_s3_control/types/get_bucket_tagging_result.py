"""Generated from Smithy shape ``com.amazonaws.s3control#GetBucketTaggingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.s3_tag_set


class GetBucketTaggingResult(TypedDict, closed=True):
    tag_set: "capo_s3_control.types.s3_tag_set.S3TagSet"
    """<p>The tags set of the Outposts bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketTaggingResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.s3_tag_set

    capo_s3_control.types.s3_tag_set.serialize_xml(value["tag_set"], el, "TagSet")


def deserialize_xml(el: Element) -> GetBucketTaggingResult:
    out: GetBucketTaggingResult = {}  # type: ignore[typeddict-item]
    child_tag_set = el.find("TagSet")
    if child_tag_set is not None:
        import capo_s3_control.types.s3_tag_set

        out["tag_set"] = capo_s3_control.types.s3_tag_set.deserialize_xml(child_tag_set)
    else:
        out["tag_set"] = []
    return out
