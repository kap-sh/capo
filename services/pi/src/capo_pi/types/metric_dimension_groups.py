"""Generated from Smithy shape ``com.amazonaws.pi#MetricDimensionGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.dimension_group_detail_list
    import capo_pi.types.string


class MetricDimensionGroups(TypedDict, closed=True):
    metric: NotRequired["capo_pi.types.string.String"]
    """<p>The metric type to which the dimension information belongs.</p>"""
    groups: NotRequired[
        "capo_pi.types.dimension_group_detail_list.DimensionGroupDetailList"
    ]
    """<p>The available dimension groups for a metric type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimensionGroups) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "groups" in value:
        import capo_pi.types.dimension_group_detail_list

        out["Groups"] = (
            capo_pi.types.dimension_group_detail_list.serialize_aws_json_1_1(
                value["groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDimensionGroups:
    out: MetricDimensionGroups = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("Groups") is not None:
        import capo_pi.types.dimension_group_detail_list

        out["groups"] = (
            capo_pi.types.dimension_group_detail_list.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricDimensionGroups) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "groups" in value:
        import capo_pi.types.dimension_group_detail_list

        out["Groups"] = capo_pi.types.dimension_group_detail_list.serialize_cbor(
            value["groups"]
        )
    return out


def deserialize_cbor(data: dict) -> MetricDimensionGroups:
    out: MetricDimensionGroups = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("Groups") is not None:
        import capo_pi.types.dimension_group_detail_list

        out["groups"] = capo_pi.types.dimension_group_detail_list.deserialize_cbor(
            data["Groups"]
        )
    return out
