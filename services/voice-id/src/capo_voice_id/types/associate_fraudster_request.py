"""Generated from Smithy shape ``com.amazonaws.voiceid#AssociateFraudsterRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.fraudster_id
    import capo_voice_id.types.watchlist_id


class AssociateFraudsterRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain that contains the fraudster.</p>"""
    watchlist_id: "capo_voice_id.types.watchlist_id.WatchlistId"
    """<p>The identifier of the watchlist you want to associate with the fraudster.</p>"""
    fraudster_id: "capo_voice_id.types.fraudster_id.FraudsterId"
    """<p>The identifier of the fraudster to be associated with the watchlist.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateFraudsterRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["WatchlistId"] = value["watchlist_id"]
    out["FraudsterId"] = value["fraudster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateFraudsterRequest:
    out: AssociateFraudsterRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("AssociateFraudsterRequest.domain_id required")
    if data.get("WatchlistId") is not None:
        out["watchlist_id"] = data["WatchlistId"]
    else:
        raise DeserializationError("AssociateFraudsterRequest.watchlist_id required")
    if data.get("FraudsterId") is not None:
        out["fraudster_id"] = data["FraudsterId"]
    else:
        raise DeserializationError("AssociateFraudsterRequest.fraudster_id required")
    return out


def redact_sensitive(value: AssociateFraudsterRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fraudster_id" in value:
        out["fraudster_id"] = "*** Sensitive Data Redacted ***"
    return out
