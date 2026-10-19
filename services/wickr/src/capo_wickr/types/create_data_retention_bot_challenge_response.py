"""Generated from Smithy shape ``com.amazonaws.wickr#CreateDataRetentionBotChallengeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.sensitive_string


class CreateDataRetentionBotChallengeResponse(TypedDict, closed=True):
    challenge: "capo_wickr.types.sensitive_string.SensitiveString"
    """<p>The newly generated challenge password for the data retention bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataRetentionBotChallengeResponse) -> dict:
    out: dict = {}
    out["challenge"] = value["challenge"]
    return out


def deserialize_json(data: dict) -> CreateDataRetentionBotChallengeResponse:
    out: CreateDataRetentionBotChallengeResponse = {}  # type: ignore[typeddict-item]
    if data.get("challenge") is not None:
        out["challenge"] = data["challenge"]
    else:
        out["challenge"] = ""
    return out


def redact_sensitive(value: CreateDataRetentionBotChallengeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "challenge" in value:
        out["challenge"] = "*** Sensitive Data Redacted ***"
    return out
