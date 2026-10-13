"""Generated from Smithy shape ``com.amazonaws.voiceid#WatchlistSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.watchlist_summary

WatchlistSummaries: TypeAlias = list[
    "capo_voice_id.types.watchlist_summary.WatchlistSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WatchlistSummaries) -> list:
    import capo_voice_id.types.watchlist_summary

    out: list = []
    for item in value:
        out.append(capo_voice_id.types.watchlist_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> WatchlistSummaries:
    import capo_voice_id.types.watchlist_summary

    out: WatchlistSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_voice_id.types.watchlist_summary.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: WatchlistSummaries) -> list[Any]:
    import capo_voice_id.types.watchlist_summary

    return [
        capo_voice_id.types.watchlist_summary.redact_sensitive(item) for item in value
    ]
