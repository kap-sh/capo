"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricData``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_datum

MetricData: TypeAlias = list["capo_cloudwatch.types.metric_datum.MetricDatum"]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_datum

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_datum.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricData:
    import capo_cloudwatch.types.metric_datum

    out: MetricData = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.metric_datum.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_datum

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_datum.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> MetricData:
    import capo_cloudwatch.types.metric_datum

    out: MetricData = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.metric_datum.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricData) -> list:
    import capo_cloudwatch.types.metric_datum

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.metric_datum.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> MetricData:
    import capo_cloudwatch.types.metric_datum

    out: MetricData = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.metric_datum.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricData) -> list:
    import capo_cloudwatch.types.metric_datum

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.metric_datum.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricData:
    import capo_cloudwatch.types.metric_datum

    out: MetricData = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.metric_datum.deserialize_cbor(item))
    return out
