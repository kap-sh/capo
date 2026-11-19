"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRuleAndOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.prefix
    import capo_s3.types.replication_rule_not_operator
    import capo_s3.types.tag_set

ReplicationRuleAndOperator = TypedDict(
    "ReplicationRuleAndOperator",
    {
        "prefix": NotRequired["capo_s3.types.prefix.Prefix"],
        "tags": NotRequired["capo_s3.types.tag_set.TagSet"],
        "not": NotRequired[
            "capo_s3.types.replication_rule_not_operator.ReplicationRuleNotOperator"
        ],
    },
    closed=True,
)


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRuleAndOperator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tags" in value:
        import capo_s3.types.tag_set

        capo_s3.types.tag_set.serialize_xml_flat(value["tags"], el, "Tag")
    if "not" in value:
        import capo_s3.types.replication_rule_not_operator

        capo_s3.types.replication_rule_not_operator.serialize_xml(
            value["not"], el, "Not"
        )


def deserialize_xml(el: Element) -> ReplicationRuleAndOperator:
    out: ReplicationRuleAndOperator = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    if el.find("Tag") is not None:
        import capo_s3.types.tag_set

        out["tags"] = capo_s3.types.tag_set.deserialize_xml_flat(el, "Tag")
    child_not = el.find("Not")
    if child_not is not None:
        import capo_s3.types.replication_rule_not_operator

        out["not"] = capo_s3.types.replication_rule_not_operator.deserialize_xml(
            child_not
        )
    return out
