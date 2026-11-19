"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_data_query

MetricDataQueries: TypeAlias = list[
    "capo_cloudwatch.types.metric_data_query.MetricDataQuery"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataQueries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_data_query

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_data_query.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricDataQueries:
    import capo_cloudwatch.types.metric_data_query

    out: MetricDataQueries = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.metric_data_query.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricDataQueries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_data_query

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_data_query.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> MetricDataQueries:
    import capo_cloudwatch.types.metric_data_query

    out: MetricDataQueries = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.metric_data_query.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDataQueries) -> list:
    import capo_cloudwatch.types.metric_data_query

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.metric_data_query.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> MetricDataQueries:
    import capo_cloudwatch.types.metric_data_query

    out: MetricDataQueries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.metric_data_query.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricDataQueries) -> list:
    import capo_cloudwatch.types.metric_data_query

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.metric_data_query.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricDataQueries:
    import capo_cloudwatch.types.metric_data_query

    out: MetricDataQueries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.metric_data_query.deserialize_cbor(item))
    return out
