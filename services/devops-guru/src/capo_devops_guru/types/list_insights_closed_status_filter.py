"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsClosedStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_guru.types.end_time_range
    import capo_devops_guru.types.insight_type


class ListInsightsClosedStatusFilter(TypedDict, closed=True):
    type: "capo_devops_guru.types.insight_type.InsightType"
    """<p> Use to filter for either <code>REACTIVE</code> or <code>PROACTIVE</code> insights. </p>"""
    end_time_range: "capo_devops_guru.types.end_time_range.EndTimeRange"
    """<p> A time range used to specify when the behavior of the filtered insights ended. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsClosedStatusFilter) -> dict:
    out: dict = {}
    import capo_devops_guru.types.insight_type

    out["Type"] = capo_devops_guru.types.insight_type.serialize_json(value["type"])
    import capo_devops_guru.types.end_time_range

    out["EndTimeRange"] = capo_devops_guru.types.end_time_range.serialize_json(
        value["end_time_range"]
    )
    return out


def deserialize_json(data: dict) -> ListInsightsClosedStatusFilter:
    out: ListInsightsClosedStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_devops_guru.types.insight_type

        out["type"] = capo_devops_guru.types.insight_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_devops_guru.types.insight_type.InsightType", "")
    if data.get("EndTimeRange") is not None:
        import capo_devops_guru.types.end_time_range

        out["end_time_range"] = capo_devops_guru.types.end_time_range.deserialize_json(
            data["EndTimeRange"]
        )
    else:
        raise DeserializationError(
            "ListInsightsClosedStatusFilter.end_time_range required"
        )
    return out
