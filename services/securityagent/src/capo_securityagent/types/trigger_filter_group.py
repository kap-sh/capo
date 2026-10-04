"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerFilterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.trigger_event_list
    import capo_securityagent.types.trigger_filter_list


class TriggerFilterGroup(TypedDict, closed=True):
    events: NotRequired["capo_securityagent.types.trigger_event_list.TriggerEventList"]
    """<p>Passes when the pull request event is one of the listed events. If you omit this, the group matches <code>PULL_REQUEST_READY_FOR_REVIEW</code> and <code>PULL_REQUEST_DRAFT</code> events only.</p>"""
    filters: NotRequired[
        "capo_securityagent.types.trigger_filter_list.TriggerFilterList"
    ]
    """<p>Passes when every filter passes. If you omit this, the group matches its events on any target branch and with any labels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerFilterGroup) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_securityagent.types.trigger_event_list

        out["events"] = capo_securityagent.types.trigger_event_list.serialize_json(
            value["events"]
        )
    if "filters" in value:
        import capo_securityagent.types.trigger_filter_list

        out["filters"] = capo_securityagent.types.trigger_filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> TriggerFilterGroup:
    out: TriggerFilterGroup = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_securityagent.types.trigger_event_list

        out["events"] = capo_securityagent.types.trigger_event_list.deserialize_json(
            data["events"]
        )
    if data.get("filters") is not None:
        import capo_securityagent.types.trigger_filter_list

        out["filters"] = capo_securityagent.types.trigger_filter_list.deserialize_json(
            data["filters"]
        )
    return out
