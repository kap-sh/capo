"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DimensionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dimension_filter

DimensionFilters: TypeAlias = list[
    "capo_cloudwatch.types.dimension_filter.DimensionFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DimensionFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.dimension_filter

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.dimension_filter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DimensionFilters:
    import capo_cloudwatch.types.dimension_filter

    out: DimensionFilters = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.dimension_filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DimensionFilters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.dimension_filter

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.dimension_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DimensionFilters:
    import capo_cloudwatch.types.dimension_filter

    out: DimensionFilters = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.dimension_filter.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionFilters) -> list:
    import capo_cloudwatch.types.dimension_filter

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.dimension_filter.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DimensionFilters:
    import capo_cloudwatch.types.dimension_filter

    out: DimensionFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.dimension_filter.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionFilters) -> list:
    import capo_cloudwatch.types.dimension_filter

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.dimension_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DimensionFilters:
    import capo_cloudwatch.types.dimension_filter

    out: DimensionFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.dimension_filter.deserialize_cbor(item))
    return out
