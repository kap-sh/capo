"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamEntries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_stream_entry

MetricStreamEntries: TypeAlias = list[
    "capo_cloudwatch.types.metric_stream_entry.MetricStreamEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricStreamEntries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_stream_entry

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_stream_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricStreamEntries:
    import capo_cloudwatch.types.metric_stream_entry

    out: MetricStreamEntries = []
    for child in el.findall("member"):
        out.append(capo_cloudwatch.types.metric_stream_entry.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricStreamEntries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.metric_stream_entry

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.metric_stream_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> MetricStreamEntries:
    import capo_cloudwatch.types.metric_stream_entry

    out: MetricStreamEntries = []
    for child in parent.findall(tag):
        out.append(capo_cloudwatch.types.metric_stream_entry.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricStreamEntries) -> list:
    import capo_cloudwatch.types.metric_stream_entry

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.metric_stream_entry.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricStreamEntries:
    import capo_cloudwatch.types.metric_stream_entry

    out: MetricStreamEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.metric_stream_entry.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricStreamEntries) -> list:
    import capo_cloudwatch.types.metric_stream_entry

    out: list = []
    for item in value:
        out.append(capo_cloudwatch.types.metric_stream_entry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricStreamEntries:
    import capo_cloudwatch.types.metric_stream_entry

    out: MetricStreamEntries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch.types.metric_stream_entry.deserialize_cbor(item))
    return out
