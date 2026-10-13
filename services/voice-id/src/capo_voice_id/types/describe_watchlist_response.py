"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeWatchlistResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.watchlist


class DescribeWatchlistResponse(TypedDict, closed=True):
    watchlist: NotRequired["capo_voice_id.types.watchlist.Watchlist"]
    """<p>Information about the specified watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeWatchlistResponse) -> dict:
    out: dict = {}
    if "watchlist" in value:
        import capo_voice_id.types.watchlist

        out["Watchlist"] = capo_voice_id.types.watchlist.serialize_aws_json_1_0(
            value["watchlist"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeWatchlistResponse:
    out: DescribeWatchlistResponse = {}  # type: ignore[typeddict-item]
    if data.get("Watchlist") is not None:
        import capo_voice_id.types.watchlist

        out["watchlist"] = capo_voice_id.types.watchlist.deserialize_aws_json_1_0(
            data["Watchlist"]
        )
    return out


def redact_sensitive(value: DescribeWatchlistResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "watchlist" in value:
        import capo_voice_id.types.watchlist

        out["watchlist"] = capo_voice_id.types.watchlist.redact_sensitive(
            value["watchlist"]
        )
    return out
