"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dimension

Dimensions: TypeAlias = list["capo_cloudwatch.types.dimension.Dimension"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Dimensions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.dimension

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.dimension.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Dimensions:
    import capo_cloudwatch.types.dimension

    out: Dimensions = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.dimension.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Dimensions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.dimension

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.dimension.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Dimensions:
    import capo_cloudwatch.types.dimension

    out: Dimensions = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.dimension.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimensions) -> list:
    import capo_cloudwatch.types.dimension

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.dimension.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Dimensions:
    import capo_cloudwatch.types.dimension

    out: Dimensions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.dimension.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Dimensions) -> list:
    import capo_cloudwatch.types.dimension

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.dimension.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Dimensions:
    import capo_cloudwatch.types.dimension

    out: Dimensions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.dimension.deserialize_cbor(item))
    return out
