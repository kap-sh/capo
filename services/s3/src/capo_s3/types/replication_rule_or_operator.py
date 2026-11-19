"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRuleOrOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.replication_prefix_list
    import capo_s3.types.tag_set


class ReplicationRuleOrOperator(TypedDict, closed=True):
    prefixes: NotRequired["capo_s3.types.replication_prefix_list.ReplicationPrefixList"]
    """<p>An array of object key name prefixes.</p>"""
    tags: NotRequired["capo_s3.types.tag_set.TagSet"]
    """<p>An array of tags containing key and value pairs.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRuleOrOperator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefixes" in value:
        import capo_s3.types.replication_prefix_list

        capo_s3.types.replication_prefix_list.serialize_xml_flat(
            value["prefixes"], el, "Prefix"
        )
    if "tags" in value:
        import capo_s3.types.tag_set

        capo_s3.types.tag_set.serialize_xml_flat(value["tags"], el, "Tag")


def deserialize_xml(el: Element) -> ReplicationRuleOrOperator:
    out: ReplicationRuleOrOperator = {}  # type: ignore[typeddict-item]
    if el.find("Prefix") is not None:
        import capo_s3.types.replication_prefix_list

        out["prefixes"] = capo_s3.types.replication_prefix_list.deserialize_xml_flat(
            el, "Prefix"
        )
    if el.find("Tag") is not None:
        import capo_s3.types.tag_set

        out["tags"] = capo_s3.types.tag_set.deserialize_xml_flat(el, "Tag")
    return out
