"""Generated from Smithy shape ``com.amazonaws.dsql#MetricGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.metric_group


class MetricGroupRequest(TypedDict, closed=True):
    metric_group: "capo_dsql.types.metric_group.MetricGroup"
    """<p>The name of the metric group to enable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricGroupRequest) -> dict:
    out: dict = {}
    import capo_dsql.types.metric_group

    out["metricGroup"] = capo_dsql.types.metric_group.serialize_json(
        value["metric_group"]
    )
    return out


def deserialize_json(data: dict) -> MetricGroupRequest:
    out: MetricGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("metricGroup") is not None:
        import capo_dsql.types.metric_group

        out["metric_group"] = capo_dsql.types.metric_group.deserialize_json(
            data["metricGroup"]
        )
    else:
        import typing

        out["metric_group"] = typing.cast(
            "capo_dsql.types.metric_group.MetricGroup", ""
        )
    return out
