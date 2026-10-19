"""Generated from Smithy shape ``com.amazonaws.personalizeevents#MetricAttribution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize_events.types.event_attribution_source


class MetricAttribution(TypedDict, closed=True):
    event_attribution_source: (
        "capo_personalize_events.types.event_attribution_source.EventAttributionSource"
    )
    """<p>The source of the event, such as a third party.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricAttribution) -> dict:
    out: dict = {}
    out["eventAttributionSource"] = value["event_attribution_source"]
    return out


def deserialize_json(data: dict) -> MetricAttribution:
    out: MetricAttribution = {}  # type: ignore[typeddict-item]
    if data.get("eventAttributionSource") is not None:
        out["event_attribution_source"] = data["eventAttributionSource"]
    else:
        out["event_attribution_source"] = ""
    return out
