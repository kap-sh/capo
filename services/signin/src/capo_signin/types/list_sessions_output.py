"""Generated from Smithy shape ``com.amazonaws.signin#ListSessionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.next_token
    import capo_signin.types.session_summary_list


class ListSessionsOutput(TypedDict, closed=True):
    items: "capo_signin.types.session_summary_list.SessionSummaryList"
    """List of session summaries"""
    next_token: NotRequired["capo_signin.types.next_token.NextToken"]
    """Token for next page of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsOutput) -> dict:
    out: dict = {}
    import capo_signin.types.session_summary_list

    out["items"] = capo_signin.types.session_summary_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionsOutput:
    out: ListSessionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_signin.types.session_summary_list

        out["items"] = capo_signin.types.session_summary_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
