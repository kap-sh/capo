"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListHealthEventsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.health_event_list


class ListHealthEventsOutput(TypedDict, closed=True):
    health_events: "capo_internetmonitor.types.health_event_list.HealthEventList"
    """<p>A list of health events.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHealthEventsOutput) -> dict:
    out: dict = {}
    import capo_internetmonitor.types.health_event_list

    out["HealthEvents"] = capo_internetmonitor.types.health_event_list.serialize_json(
        value["health_events"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHealthEventsOutput:
    out: ListHealthEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("HealthEvents") is not None:
        import capo_internetmonitor.types.health_event_list

        out["health_events"] = (
            capo_internetmonitor.types.health_event_list.deserialize_json(
                data["HealthEvents"]
            )
        )
    else:
        out["health_events"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
