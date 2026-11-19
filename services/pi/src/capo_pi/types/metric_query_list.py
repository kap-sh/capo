"""Generated from Smithy shape ``com.amazonaws.pi#MetricQueryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.metric_query

MetricQueryList: TypeAlias = list["capo_pi.types.metric_query.MetricQuery"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricQueryList) -> list:
    import capo_pi.types.metric_query

    out: list = []
    for item in value:
        out.append(capo_pi.types.metric_query.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricQueryList:
    import capo_pi.types.metric_query

    out: MetricQueryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.metric_query.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricQueryList) -> list:
    import capo_pi.types.metric_query

    out: list = []
    for item in value:
        out.append(capo_pi.types.metric_query.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricQueryList:
    import capo_pi.types.metric_query

    out: MetricQueryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.metric_query.deserialize_cbor(item))
    return out
