"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ManagedRules``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.managed_rule

ManagedRules: TypeAlias = list["capo_cloudwatch.types.managed_rule.ManagedRule"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedRules, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.managed_rule

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.managed_rule.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ManagedRules:
    import capo_cloudwatch.types.managed_rule

    out: ManagedRules = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.managed_rule.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ManagedRules, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.managed_rule

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.managed_rule.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ManagedRules:
    import capo_cloudwatch.types.managed_rule

    out: ManagedRules = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.managed_rule.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedRules) -> list:
    import capo_cloudwatch.types.managed_rule

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.managed_rule.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ManagedRules:
    import capo_cloudwatch.types.managed_rule

    out: ManagedRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.managed_rule.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ManagedRules) -> list:
    import capo_cloudwatch.types.managed_rule

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.managed_rule.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ManagedRules:
    import capo_cloudwatch.types.managed_rule

    out: ManagedRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.managed_rule.deserialize_cbor(item))
    return out
