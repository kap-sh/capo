"""Generated from Smithy shape ``com.amazonaws.voiceid#WatchlistDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.watchlist_id


class WatchlistDetails(TypedDict, closed=True):
    default_watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the default watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WatchlistDetails) -> dict:
    out: dict = {}
    out["DefaultWatchlistId"] = value["default_watchlist_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WatchlistDetails:
    out: WatchlistDetails = {}  # type: ignore[typeddict-item]
    if data.get("DefaultWatchlistId") is not None:
        out["default_watchlist_id"] = data["DefaultWatchlistId"]
    else:
        out["default_watchlist_id"] = ""
    return out
