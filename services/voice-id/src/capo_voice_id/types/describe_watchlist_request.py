"""Generated from Smithy shape ``com.amazonaws.voiceid#DescribeWatchlistRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.watchlist_id


class DescribeWatchlistRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the watchlist.</p>"""
    watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the watchlist that you are describing.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeWatchlistRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["WatchlistId"] = value["watchlist_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeWatchlistRequest:
    out: DescribeWatchlistRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    if data.get("WatchlistId") is not None:
        out["watchlist_id"] = data["WatchlistId"]
    else:
        out["watchlist_id"] = ""
    return out
