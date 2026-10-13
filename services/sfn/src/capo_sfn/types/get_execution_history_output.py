"""Generated from Smithy shape ``com.amazonaws.sfn#GetExecutionHistoryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.history_event_list
    import capo_sfn.types.page_token


class GetExecutionHistoryOutput(TypedDict, closed=True):
    events: "capo_sfn.types.history_event_list.HistoryEventList"
    """<p>The list of events that occurred in the execution.</p>"""
    next_token: NotRequired["capo_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetExecutionHistoryOutput) -> dict:
    out: dict = {}
    import capo_sfn.types.history_event_list

    out["events"] = capo_sfn.types.history_event_list.serialize_aws_json_1_0(
        value["events"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetExecutionHistoryOutput:
    out: GetExecutionHistoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_sfn.types.history_event_list

        out["events"] = capo_sfn.types.history_event_list.deserialize_aws_json_1_0(
            data["events"]
        )
    else:
        raise DeserializationError("GetExecutionHistoryOutput.events required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: GetExecutionHistoryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events" in value:
        import capo_sfn.types.history_event_list

        out["events"] = capo_sfn.types.history_event_list.redact_sensitive(
            value["events"]
        )
    return out
