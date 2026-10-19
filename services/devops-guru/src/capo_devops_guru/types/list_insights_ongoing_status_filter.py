"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsOngoingStatusFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_type


class ListInsightsOngoingStatusFilter(TypedDict, closed=True):
    type: "capo_devops_guru.types.insight_type.InsightType"
    """<p> Use to filter for either <code>REACTIVE</code> or <code>PROACTIVE</code> insights. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsOngoingStatusFilter) -> dict:
    out: dict = {}
    import capo_devops_guru.types.insight_type

    out["Type"] = capo_devops_guru.types.insight_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> ListInsightsOngoingStatusFilter:
    out: ListInsightsOngoingStatusFilter = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_devops_guru.types.insight_type

        out["type"] = capo_devops_guru.types.insight_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_devops_guru.types.insight_type.InsightType", "")
    return out
