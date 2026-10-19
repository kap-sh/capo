"""Generated from Smithy shape ``com.amazonaws.s3#GetObjectTaggingOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_version_id
    import capo_s3.types.tag_set


class GetObjectTaggingOutput(TypedDict, closed=True):
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The versionId of the object for which you got the tagging information.</p>"""
    tag_set: "capo_s3.types.tag_set.TagSet"
    """<p>Contains the tag set.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetObjectTaggingOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.tag_set

    capo_s3.types.tag_set.serialize_xml(value["tag_set"], el, "TagSet")


def deserialize_xml(el: Element) -> GetObjectTaggingOutput:
    out: GetObjectTaggingOutput = {}  # type: ignore[typeddict-item]
    child_tag_set = el.find("TagSet")
    if child_tag_set is not None:
        import capo_s3.types.tag_set

        out["tag_set"] = capo_s3.types.tag_set.deserialize_xml(child_tag_set)
    else:
        out["tag_set"] = []
    return out
