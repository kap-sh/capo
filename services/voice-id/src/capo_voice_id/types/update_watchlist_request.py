"""Generated from Smithy shape ``com.amazonaws.voiceid#UpdateWatchlistRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.watchlist_description
    import capo_voice_id.types.watchlist_id
    import capo_voice_id.types.watchlist_name


class UpdateWatchlistRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the watchlist.</p>"""
    watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the watchlist to be updated.</p>"""
    name: NotRequired["capo_voice_id.types.watchlist_name.WatchlistName"]
    """<p>The name of the watchlist.</p>"""
    description: NotRequired[
        "capo_voice_id.types.watchlist_description.WatchlistDescription"
    ]
    """<p>A brief description about this watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWatchlistRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["WatchlistId"] = value["watchlist_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWatchlistRequest:
    out: UpdateWatchlistRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    if data.get("WatchlistId") is not None:
        out["watchlist_id"] = data["WatchlistId"]
    else:
        out["watchlist_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: UpdateWatchlistRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
