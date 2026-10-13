"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ListStreamSessionsByAccountOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.next_token
    import capo_gameliftstreams.types.stream_session_summary_list


class ListStreamSessionsByAccountOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_gameliftstreams.types.stream_session_summary_list.StreamSessionSummaryList"
    ]
    """<p>A collection of Amazon GameLift Streams stream sessions that are associated with a stream group and returned in response to a list request. Each item includes stream session metadata and status.</p>"""
    next_token: NotRequired["capo_gameliftstreams.types.next_token.NextToken"]
    """<p>A token that marks the start of the next sequential page of results. If an operation doesn't return a token, you've reached the end of the list. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamSessionsByAccountOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_gameliftstreams.types.stream_session_summary_list

        out["Items"] = (
            capo_gameliftstreams.types.stream_session_summary_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStreamSessionsByAccountOutput:
    out: ListStreamSessionsByAccountOutput = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_gameliftstreams.types.stream_session_summary_list

        out["items"] = (
            capo_gameliftstreams.types.stream_session_summary_list.deserialize_json(
                data["Items"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListStreamSessionsByAccountOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_gameliftstreams.types.stream_session_summary_list

        out["items"] = (
            capo_gameliftstreams.types.stream_session_summary_list.redact_sensitive(
                value["items"]
            )
        )
    return out
