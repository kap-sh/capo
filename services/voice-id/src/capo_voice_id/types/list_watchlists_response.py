"""Generated from Smithy shape ``com.amazonaws.voiceid#ListWatchlistsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.string
    import capo_voice_id.types.watchlist_summaries


class ListWatchlistsResponse(TypedDict, closed=True):
    watchlist_summaries: NotRequired[
        "capo_voice_id.types.watchlist_summaries.WatchlistSummaries"
    ]
    """<p>A list that contains details about each watchlist in the Amazon Web Services account. </p>"""
    next_token: NotRequired["capo_voice_id.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWatchlistsResponse) -> dict:
    out: dict = {}
    if "watchlist_summaries" in value:
        import capo_voice_id.types.watchlist_summaries

        out["WatchlistSummaries"] = (
            capo_voice_id.types.watchlist_summaries.serialize_aws_json_1_0(
                value["watchlist_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWatchlistsResponse:
    out: ListWatchlistsResponse = {}  # type: ignore[typeddict-item]
    if data.get("WatchlistSummaries") is not None:
        import capo_voice_id.types.watchlist_summaries

        out["watchlist_summaries"] = (
            capo_voice_id.types.watchlist_summaries.deserialize_aws_json_1_0(
                data["WatchlistSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListWatchlistsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "watchlist_summaries" in value:
        import capo_voice_id.types.watchlist_summaries

        out["watchlist_summaries"] = (
            capo_voice_id.types.watchlist_summaries.redact_sensitive(
                value["watchlist_summaries"]
            )
        )
    return out
