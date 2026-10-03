"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignEventFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.event_dimensions
    import capo_pinpoint.types.filter_type


class CampaignEventFilter(TypedDict, closed=True):
    dimensions: NotRequired["capo_pinpoint.types.event_dimensions.EventDimensions"]
    """<p>The dimension settings of the event filter for the campaign.</p>"""
    filter_type: NotRequired["capo_pinpoint.types.filter_type.FilterType"]
    """<p>The type of event that causes the campaign to be sent. Valid values are: SYSTEM, sends the campaign when a system event occurs; and, ENDPOINT, sends the campaign when an endpoint event (<link linkend="apps-application-id-events">Events</link> resource) occurs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignEventFilter) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_pinpoint.types.event_dimensions

        out["Dimensions"] = capo_pinpoint.types.event_dimensions.serialize_json(
            value["dimensions"]
        )
    if "filter_type" in value:
        import capo_pinpoint.types.filter_type

        out["FilterType"] = capo_pinpoint.types.filter_type.serialize_json(
            value["filter_type"]
        )
    return out


def deserialize_json(data: dict) -> CampaignEventFilter:
    out: CampaignEventFilter = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_pinpoint.types.event_dimensions

        out["dimensions"] = capo_pinpoint.types.event_dimensions.deserialize_json(
            data["Dimensions"]
        )
    if data.get("FilterType") is not None:
        import capo_pinpoint.types.filter_type

        out["filter_type"] = capo_pinpoint.types.filter_type.deserialize_json(
            data["FilterType"]
        )
    return out
