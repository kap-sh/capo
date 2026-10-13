"""Generated from Smithy shape ``com.amazonaws.voiceid#WatchlistSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.boolean
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.timestamp
    import capo_voice_id.types.watchlist_description
    import capo_voice_id.types.watchlist_id
    import capo_voice_id.types.watchlist_name


class WatchlistSummary(TypedDict, closed=True):
    domain_id: NotRequired["capo_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the watchlist.</p>"""
    watchlist_id: NotRequired["capo_voice_id.types.watchlist_id.WatchlistId"]
    """<p>The identifier of the watchlist.</p>"""
    name: NotRequired["capo_voice_id.types.watchlist_name.WatchlistName"]
    """<p>The name for the watchlist.</p>"""
    description: NotRequired[
        "capo_voice_id.types.watchlist_description.WatchlistDescription"
    ]
    """<p>The description of the watchlist.</p>"""
    default_watchlist: "capo_voice_id.types.boolean.Boolean"
    """<p>Whether the specified watchlist is the default watchlist of a domain.</p>"""
    created_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the watchlist was created.</p>"""
    updated_at: NotRequired["capo_voice_id.types.timestamp.Timestamp"]
    """<p>The timestamp of when the watchlist was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WatchlistSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "watchlist_id" in value:
        out["WatchlistId"] = value["watchlist_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["DefaultWatchlist"] = value.get("default_watchlist", False)
    if "created_at" in value:
        import capo_voice_id.types.timestamp

        out["CreatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_voice_id.types.timestamp

        out["UpdatedAt"] = capo_voice_id.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> WatchlistSummary:
    out: WatchlistSummary = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    if data.get("WatchlistId") is not None:
        out["watchlist_id"] = data["WatchlistId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DefaultWatchlist") is not None:
        out["default_watchlist"] = data["DefaultWatchlist"]
    else:
        out["default_watchlist"] = False
    if data.get("CreatedAt") is not None:
        import capo_voice_id.types.timestamp

        out["created_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_voice_id.types.timestamp

        out["updated_at"] = capo_voice_id.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    return out


def redact_sensitive(value: WatchlistSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
