"""Generated from Smithy shape ``com.amazonaws.pi#MetricKeyDataPointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.metric_key_data_points

MetricKeyDataPointsList: TypeAlias = list[
    "capo_pi.types.metric_key_data_points.MetricKeyDataPoints"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricKeyDataPointsList) -> list:
    import capo_pi.types.metric_key_data_points

    out: list = []
    for item in value:
        out.append(capo_pi.types.metric_key_data_points.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricKeyDataPointsList:
    import capo_pi.types.metric_key_data_points

    out: MetricKeyDataPointsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.metric_key_data_points.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricKeyDataPointsList) -> list:
    import capo_pi.types.metric_key_data_points

    out: list = []
    for item in value:
        out.append(capo_pi.types.metric_key_data_points.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricKeyDataPointsList:
    import capo_pi.types.metric_key_data_points

    out: MetricKeyDataPointsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.metric_key_data_points.deserialize_cbor(item))
    return out
