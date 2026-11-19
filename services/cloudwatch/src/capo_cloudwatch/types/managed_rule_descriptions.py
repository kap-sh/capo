"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ManagedRuleDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.managed_rule_description

ManagedRuleDescriptions: TypeAlias = list[
    "capo_cloudwatch.types.managed_rule_description.ManagedRuleDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedRuleDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.managed_rule_description

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.managed_rule_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ManagedRuleDescriptions:
    import capo_cloudwatch.types.managed_rule_description

    out: ManagedRuleDescriptions = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.managed_rule_description.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ManagedRuleDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.managed_rule_description

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.managed_rule_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ManagedRuleDescriptions:
    import capo_cloudwatch.types.managed_rule_description

    out: ManagedRuleDescriptions = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.managed_rule_description.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedRuleDescriptions) -> list:
    import capo_cloudwatch.types.managed_rule_description

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.managed_rule_description.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ManagedRuleDescriptions:
    import capo_cloudwatch.types.managed_rule_description

    out: ManagedRuleDescriptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.managed_rule_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ManagedRuleDescriptions) -> list:
    import capo_cloudwatch.types.managed_rule_description

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.managed_rule_description.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ManagedRuleDescriptions:
    import capo_cloudwatch.types.managed_rule_description

    out: ManagedRuleDescriptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.managed_rule_description.deserialize_cbor(item)
        )
    return out
