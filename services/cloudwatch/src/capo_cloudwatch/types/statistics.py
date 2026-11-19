"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Statistics``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.statistic

Statistics: TypeAlias = list["capo_cloudwatch.types.statistic.Statistic"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Statistics, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.statistic

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.statistic.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Statistics:
    import capo_cloudwatch.types.statistic

    out: Statistics = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.statistic.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Statistics, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.statistic

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.statistic.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Statistics:
    import capo_cloudwatch.types.statistic

    out: Statistics = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.statistic.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Statistics) -> list:
    import capo_cloudwatch.types.statistic

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.statistic.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Statistics:
    import capo_cloudwatch.types.statistic

    out: Statistics = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.statistic.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Statistics) -> list:
    import capo_cloudwatch.types.statistic

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.statistic.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Statistics:
    import capo_cloudwatch.types.statistic

    out: Statistics = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.statistic.deserialize_cbor(item))
    return out
