"""Generated from Smithy shape ``com.amazonaws.pi#MetricDimensionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.metric_dimension_groups

MetricDimensionsList: TypeAlias = list[
    "capo_pi.types.metric_dimension_groups.MetricDimensionGroups"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimensionsList) -> list:
    import capo_pi.types.metric_dimension_groups

    out: list = []
    for item in value:
        out.append(capo_pi.types.metric_dimension_groups.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MetricDimensionsList:
    import capo_pi.types.metric_dimension_groups

    out: MetricDimensionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.metric_dimension_groups.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricDimensionsList) -> list:
    import capo_pi.types.metric_dimension_groups

    out: list = []
    for item in value:
        out.append(capo_pi.types.metric_dimension_groups.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MetricDimensionsList:
    import capo_pi.types.metric_dimension_groups

    out: MetricDimensionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.metric_dimension_groups.deserialize_cbor(item))
    return out
