"""Generated from Smithy shape ``com.amazonaws.notifications#ListEventRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.event_rules
    import capo_notifications.types.next_token


class ListEventRulesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_notifications.types.next_token.NextToken"]
    """<p>A pagination token. If a non-null pagination token is returned in a result, pass its value in another request to retrieve more entries.</p>"""
    event_rules: "capo_notifications.types.event_rules.EventRules"
    """<p>A list of <code>EventRules</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_notifications.types.event_rules

    out["eventRules"] = capo_notifications.types.event_rules.serialize_json(
        value["event_rules"]
    )
    return out


def deserialize_json(data: dict) -> ListEventRulesResponse:
    out: ListEventRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("eventRules") is not None:
        import capo_notifications.types.event_rules

        out["event_rules"] = capo_notifications.types.event_rules.deserialize_json(
            data["eventRules"]
        )
    else:
        out["event_rules"] = []
    return out
