"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListEventsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.event_list
    import capo_bedrock_agentcore.types.pagination_token


class ListEventsOutput(TypedDict, closed=True):
    events: "capo_bedrock_agentcore.types.event_list.EventList"
    """<p>The list of events that match the specified criteria.</p>"""
    next_token: NotRequired[
        "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventsOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.event_list

    out["events"] = capo_bedrock_agentcore.types.event_list.serialize_json(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventsOutput:
    out: ListEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_bedrock_agentcore.types.event_list

        out["events"] = capo_bedrock_agentcore.types.event_list.deserialize_json(
            data["events"]
        )
    else:
        out["events"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListEventsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events" in value:
        import capo_bedrock_agentcore.types.event_list

        out["events"] = capo_bedrock_agentcore.types.event_list.redact_sensitive(
            value["events"]
        )
    return out
