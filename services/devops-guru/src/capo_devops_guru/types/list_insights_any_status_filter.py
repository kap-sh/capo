"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsAnyStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_type
    import capo_devops_guru.types.start_time_range


class ListInsightsAnyStatusFilter(TypedDict, closed=True):
    type: "capo_devops_guru.types.insight_type.InsightType"
    """<p> Use to filter for either <code>REACTIVE</code> or <code>PROACTIVE</code> insights. </p>"""
    start_time_range: "capo_devops_guru.types.start_time_range.StartTimeRange"
    """<p> A time range used to specify when the behavior of the filtered insights started. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsAnyStatusFilter) -> dict:
    out: dict = {}
    import capo_devops_guru.types.insight_type

    out["Type"] = capo_devops_guru.types.insight_type.serialize_json(value["type"])
    import capo_devops_guru.types.start_time_range

    out["StartTimeRange"] = capo_devops_guru.types.start_time_range.serialize_json(
        value["start_time_range"]
    )
    return out


def deserialize_json(data: dict) -> ListInsightsAnyStatusFilter:
    out: ListInsightsAnyStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_devops_guru.types.insight_type

        out["type"] = capo_devops_guru.types.insight_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_devops_guru.types.insight_type.InsightType", "")
    if data.get("StartTimeRange") is not None:
        import capo_devops_guru.types.start_time_range

        out["start_time_range"] = (
            capo_devops_guru.types.start_time_range.deserialize_json(
                data["StartTimeRange"]
            )
        )
    else:
        raise DeserializationError(
            "ListInsightsAnyStatusFilter.start_time_range required"
        )
    return out
