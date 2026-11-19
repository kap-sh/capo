"""Generated from Smithy shape ``com.amazonaws.pi#ResponseResourceMetricList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.response_resource_metric

ResponseResourceMetricList: TypeAlias = list[
    "capo_pi.types.response_resource_metric.ResponseResourceMetric"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseResourceMetricList) -> list:
    import capo_pi.types.response_resource_metric

    out: list = []
    for item in value:
        out.append(capo_pi.types.response_resource_metric.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResponseResourceMetricList:
    import capo_pi.types.response_resource_metric

    out: ResponseResourceMetricList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pi.types.response_resource_metric.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResponseResourceMetricList) -> list:
    import capo_pi.types.response_resource_metric

    out: list = []
    for item in value:
        out.append(capo_pi.types.response_resource_metric.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ResponseResourceMetricList:
    import capo_pi.types.response_resource_metric

    out: ResponseResourceMetricList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.response_resource_metric.deserialize_cbor(item))
    return out
