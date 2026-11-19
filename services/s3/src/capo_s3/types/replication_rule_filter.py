"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRuleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.prefix
    import capo_s3.types.replication_rule_and_operator
    import capo_s3.types.replication_rule_not_operator
    import capo_s3.types.tag

ReplicationRuleFilter = TypedDict(
    "ReplicationRuleFilter",
    {
        "prefix": NotRequired["capo_s3.types.prefix.Prefix"],
        "tag": NotRequired["capo_s3.types.tag.Tag"],
        "and": NotRequired[
            "capo_s3.types.replication_rule_and_operator.ReplicationRuleAndOperator"
        ],
        "not": NotRequired[
            "capo_s3.types.replication_rule_not_operator.ReplicationRuleNotOperator"
        ],
    },
    closed=True,
)


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRuleFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "tag" in value:
        import capo_s3.types.tag

        capo_s3.types.tag.serialize_xml(value["tag"], el, "Tag")
    if "and" in value:
        import capo_s3.types.replication_rule_and_operator

        capo_s3.types.replication_rule_and_operator.serialize_xml(
            value["and"], el, "And"
        )
    if "not" in value:
        import capo_s3.types.replication_rule_not_operator

        capo_s3.types.replication_rule_not_operator.serialize_xml(
            value["not"], el, "Not"
        )


def deserialize_xml(el: Element) -> ReplicationRuleFilter:
    out: ReplicationRuleFilter = {}  # type: ignore[typeddict-item]
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_tag = el.find("Tag")
    if child_tag is not None:
        import capo_s3.types.tag

        out["tag"] = capo_s3.types.tag.deserialize_xml(child_tag)
    child_and = el.find("And")
    if child_and is not None:
        import capo_s3.types.replication_rule_and_operator

        out["and"] = capo_s3.types.replication_rule_and_operator.deserialize_xml(
            child_and
        )
    child_not = el.find("Not")
    if child_not is not None:
        import capo_s3.types.replication_rule_not_operator

        out["not"] = capo_s3.types.replication_rule_not_operator.deserialize_xml(
            child_not
        )
    return out
