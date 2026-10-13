"""Generated from Smithy shape ``com.amazonaws.lambda#GetDurableExecutionHistoryResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.events
    import capo_lambda.types.string


class GetDurableExecutionHistoryResponse(TypedDict, closed=True):
    events: "capo_lambda.types.events.Events"
    """<p>An array of execution history events, ordered chronologically unless <code>ReverseOrder</code> is set to <code>true</code>. Each event represents a significant occurrence during the execution, such as step completion or callback resolution.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>If present, indicates that more history events are available. Use this value as the <code>Marker</code> parameter in a subsequent request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDurableExecutionHistoryResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.events

    out["Events"] = capo_lambda.types.events.serialize_json(value["events"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> GetDurableExecutionHistoryResponse:
    out: GetDurableExecutionHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("Events") is not None:
        import capo_lambda.types.events

        out["events"] = capo_lambda.types.events.deserialize_json(data["Events"])
    else:
        raise DeserializationError("GetDurableExecutionHistoryResponse.events required")
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out


def redact_sensitive(value: GetDurableExecutionHistoryResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events" in value:
        import capo_lambda.types.events

        out["events"] = capo_lambda.types.events.redact_sensitive(value["events"])
    return out
