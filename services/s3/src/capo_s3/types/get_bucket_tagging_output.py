"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketTaggingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.tag_set


class GetBucketTaggingOutput(TypedDict, closed=True):
    tag_set: "capo_s3.types.tag_set.TagSet"
    """<p>Contains the tag set.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketTaggingOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.tag_set

    capo_s3.types.tag_set.serialize_xml(value["tag_set"], el, "TagSet")


def deserialize_xml(el: Element) -> GetBucketTaggingOutput:
    out: GetBucketTaggingOutput = {}  # type: ignore[typeddict-item]
    child_tag_set = el.find("TagSet")
    if child_tag_set is not None:
        import capo_s3.types.tag_set

        out["tag_set"] = capo_s3.types.tag_set.deserialize_xml(child_tag_set)
    else:
        out["tag_set"] = []
    return out
