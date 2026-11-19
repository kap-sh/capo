"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRules``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule

InsightRules: TypeAlias = list["capo_cloudwatch.types.insight_rule.InsightRule"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRules, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.insight_rule

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.insight_rule.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InsightRules:
    import capo_cloudwatch.types.insight_rule

    out: InsightRules = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.insight_rule.deserialize_query(child))
    return out


def serialize_query_flat(
    value: InsightRules, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.insight_rule

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.insight_rule.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> InsightRules:
    import capo_cloudwatch.types.insight_rule

    out: InsightRules = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.insight_rule.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRules) -> list:
    import capo_cloudwatch.types.insight_rule

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.insight_rule.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> InsightRules:
    import capo_cloudwatch.types.insight_rule

    out: InsightRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.insight_rule.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InsightRules) -> list:
    import capo_cloudwatch.types.insight_rule

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.insight_rule.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> InsightRules:
    import capo_cloudwatch.types.insight_rule

    out: InsightRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.insight_rule.deserialize_cbor(item))
    return out
