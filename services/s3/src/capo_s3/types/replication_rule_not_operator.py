"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRuleNotOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.prefix
    import capo_s3.types.replication_rule_or_operator
    import capo_s3.types.tag

ReplicationRuleNotOperator = TypedDict(
    "ReplicationRuleNotOperator",
    {
        "prefix": NotRequired["capo_s3.types.prefix.Prefix"],
        "tag": NotRequired["capo_s3.types.tag.Tag"],
        "or": NotRequired[
            "capo_s3.types.replication_rule_or_operator.ReplicationRuleOrOperator"
        ],
    },
    closed=True,
)


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRuleNotOperator, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tag" in value:
        import capo_s3.types.tag

        capo_s3.types.tag.serialize_xml(value["tag"], el, "Tag")
    if "or" in value:
        import capo_s3.types.replication_rule_or_operator

        capo_s3.types.replication_rule_or_operator.serialize_xml(value["or"], el, "Or")


def deserialize_xml(el: Element) -> ReplicationRuleNotOperator:
    out: ReplicationRuleNotOperator = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_tag = el.find("Tag")
    if child_tag is not None:
        import capo_s3.types.tag

        out["tag"] = capo_s3.types.tag.deserialize_xml(child_tag)
    child_or = el.find("Or")
    if child_or is not None:
        import capo_s3.types.replication_rule_or_operator

        out["or"] = capo_s3.types.replication_rule_or_operator.deserialize_xml(child_or)
    return out
