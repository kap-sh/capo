"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDataResults``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_data_result

MetricDataResults: TypeAlias = list[
    "capo_cloudwatch.types.metric_data_result.MetricDataResult"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataResults, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_data_result

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_data_result.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricDataResults:
    import capo_cloudwatch.types.metric_data_result

    out: MetricDataResults = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.metric_data_result.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricDataResults, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_data_result

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_data_result.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> MetricDataResults:
    import capo_cloudwatch.types.metric_data_result

    out: MetricDataResults = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.metric_data_result.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDataResults) -> list:
    import capo_cloudwatch.types.metric_data_result

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.metric_data_result.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricDataResults:
    import capo_cloudwatch.types.metric_data_result

    out: MetricDataResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.metric_data_result.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricDataResults) -> list:
    import capo_cloudwatch.types.metric_data_result

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.metric_data_result.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricDataResults:
    import capo_cloudwatch.types.metric_data_result

    out: MetricDataResults = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.metric_data_result.deserialize_cbor(item))
    return out
